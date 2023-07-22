import random

def generate():
    did=['DO']
    for i in range(4):
        did.append(str(random.randint(0,9)))
    return ''.join(did)

