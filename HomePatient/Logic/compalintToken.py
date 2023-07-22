import random

def createToken():
    token=[]
    for i in range(6):
        token.append(str(random.randint(0,9)))
    return ''.join(token)