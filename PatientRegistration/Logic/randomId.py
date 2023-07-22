import random

def generateRandomId():
    id=['PA']
    for i in range(0,4):
        value=random.randint(0,9)
        id.append(str(value))
    return ''.join(id)
