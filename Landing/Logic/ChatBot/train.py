import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random
import os

import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle

words=[]
classes = []
documents = []
ignoreLetters = ['!', '?', ',', '.']
data=json.loads(open(os.path.join('Landing','Logic','ChatBot','data.json')).read())


for nmd in data['nonMedData']:
    for pattern in nmd['patterns']:
        word = nltk.word_tokenize(pattern)
        words.extend(word)
        documents.append((word, nmd['tag']))
        if nmd['tag'] not in classes:
            classes.append(nmd['tag'])

print ('Documents created')
print("Documents [(['tokenized', 'pattern'],'tag'), ....]\n",documents[0],'\n',documents[1],'....')

classes = sorted(classes)
print ('Classes identified')

words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignoreLetters]
words = sorted(list(set(words)))
print ('Words lemmatized')

pickle.dump(words,open(os.path.join('Landing','Logic','ChatBot','words.pkl'),'wb'))
pickle.dump(classes,open(os.path.join('Landing','Logic','ChatBot','classes.pkl'),'wb'))

training = []
outputEmpty = [0] * len(classes)
for doc in documents:
    bag = []
    patternWords = doc[0]
    patternWords = [lemmatizer.lemmatize(word.lower()) for word in patternWords]
    for word in words:
        bag.append(1) if word in patternWords else bag.append(0)
    
    outputRow = list(outputEmpty)
    outputRow[classes.index(doc[1])] = 1
    training.append([bag, outputRow])

random.shuffle(training)

training = np.array(training)
train_x = list(training[:,0])
train_y = list(training[:,1])
print('Training data created')

# Create model - 3 layers. 1st layer 128 neurons, 2nd layer 64 neurons and 3rd output layer contains number of neurons
# equal to number of nonMedData tags to predict output nonMedData with softmax
model = Sequential()
model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(train_y[0]), activation='softmax'))

# Compile model, Stochastic gradient descent with Nesterov accelerated gradient
sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

#fit and save model 
hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
model.save(os.path.join('Landing','Logic','ChatBot','chatbotNMD_model.h5'), hist)

print('Model created')