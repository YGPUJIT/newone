import random

def generateRandomId(start):
    id=[start]
    for i in range(0,4):
        value=random.randint(0,9)
        id.append(str(value))
    return ''.join(id)
