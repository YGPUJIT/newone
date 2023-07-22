import random
import numpy as np
import nltk
import os
from Hospital.settings import BASE_DIR



from nltk.stem import WordNetLemmatizer
wnl = WordNetLemmatizer()

# os.path.join('Landing','Logic','ChatBot','chatbotNMD_model.h5')

from keras.models import load_model
model = load_model(os.path.join('Landing','Logic','ChatBot','chatbotNMD_model.h5'))

import json
data = json.loads(open(os.path.join('Landing','Logic','ChatBot','data.json')).read())
disease = data['diseaseList']
response = data['responseList']

import pickle
words = pickle.load(open(os.path.join('Landing','Logic','ChatBot','words.pkl'),'rb'))
classes = pickle.load(open(os.path.join('Landing','Logic','ChatBot','classes.pkl'),'rb'))


def cleanUpSentence(sentence):
    sentenceWords = nltk.word_tokenize(sentence)
    sentenceWords = [wnl.lemmatize(word.lower()) for word in sentenceWords]
    return sentenceWords

def wordsBag(sentenceWords, words, details=True):
    bag = [0]*len(words)  
    for s in sentenceWords:
        for i,word in enumerate(words):
            if word == s:
                bag[i] = 1
                if details:
                    print('found in bag: %s' % word)
    return np.array(bag)

def predictClass(sentenceWords):
    # filter below  threshold predictions
    p = wordsBag(sentenceWords, words, details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r>ERROR_THRESHOLD]

    results.sort(key=lambda x: x[1], reverse=True)
    if len(results):
        # print(classes[results[0][0]])
        return classes[results[0][0]]
    else:
        # print('noanswer')
        return 'noanswer'

def positionCheck(sentenceWords, t):
    index = sentenceWords.index(t[0]) + 1
    for j in t[1:]:
        if sentenceWords.index(j) == index:
            index+=1
        else:
            return 0
    return 1

def getResponse(sentenceWords):
    dis=''
    sentenceWordsSet=set(sentenceWords)
    for i in disease.keys():
        t = i.split()
        if len(t)-1:
            if set(t).issubset(sentenceWordsSet):
                f = positionCheck(sentenceWords, t)
                if f:
                    dis = disease.get(i)
                    break
        elif i in sentenceWordsSet:
            dis = disease.get(i)
            break
    if not dis:
        tag = predictClass(sentenceWords)
        nmdList = data['nonMedData']
        for i in nmdList:
            if i['tag']==tag:
                result = random.choice(i['responses'])
                break
        return result

    res = 'what'
    for i in response.keys():
        t = i.split()
        if len(t)-1:
            if set(t).issubset(sentenceWordsSet):
                f = positionCheck(sentenceWords, t)
                if f:
                    res = response.get(i)
                    break
        elif i in sentenceWordsSet:
            res = response.get(i)
            break
    medData = data['medData']
    for i in medData:
        if i['disease']==dis:
            return '<br>'.join(i['response'][res])


getResponse("sentenceWords")



def chatResponse(message):
    model.predict(np.array([np.array([0]*len(words))]))[0]
    msg=message
    sentenceWords = cleanUpSentence(msg)
    res = getResponse(sentenceWords)
    return res
