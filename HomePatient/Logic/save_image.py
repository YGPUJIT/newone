from django.core.files.storage import FileSystemStorage
from Hospital.settings import BASE_DIR
import os
import shutil
import cv2


def save(image_files,pid,patient):
    print("save")
    path=os.path.join(BASE_DIR,'Security','Logic','ML','FaceRec','dataset',pid+'-'+patient['first_name'])
    if(os.path.exists(path)):
        shutil.rmtree(path)
    path=os.path.join(BASE_DIR,'Security','Logic','ML','FaceRec','dataset',pid+'-'+patient['first_name'])
    fs=FileSystemStorage(path)
    images=image_files.getlist('image')
    for i,img in enumerate(images):
        # img=cv2.imread(img)
        # img=cv2.resize(img,(600,500))
        image_type='.'+img.name.split('.')[-1]
        fs.save("0000"+str(i)+image_type,img)
