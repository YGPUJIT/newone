import shutil
import os
from Hospital.settings import BASE_DIR

def clear():
    try:
        path=os.path.join(BASE_DIR,'Security','Logic','ML','FaceRec',"__pycache__")
        shutil.rmtree(path)
        path=os.path.join(BASE_DIR,'Security','Logic',"__pycache__")
        shutil.rmtree(path)
        print("cache cleared")
    except:
        return