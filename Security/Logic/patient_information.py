import os
from Hospital.settings import BASE_DIR

def getStructuredDocument(patient):
    information=[]
    pid=patient['pid']
    information.append(("Patient ID",pid))
    name=patient['first_name']+" "+patient['last_name']
    information.append(("Name",name))
    age=patient['age']
    information.append(("Age",age))
    sex=patient['sex']
    information.append(('Sex',sex))
    disease=patient['disease_actual']
    information.append(('Disease',disease))
    if(patient['initiateTreatment']):
        information.append(("Bill","Not payed"))
    symptoms_list=[]
    for s in patient['symptoms']:
        symptoms_list.append(" "+patient['symptoms'][s].upper())
    information.append(("Symptoms",symptoms_list))
    directory_name=patient['pid'].upper()+"-"+patient['first_name'].upper()
    link=os.path.join(BASE_DIR,'Security','Logic','ML','FaceRec','dataset',directory_name)
    file_name=os.listdir(link)[0]
    information.append(("href","/static/"+directory_name+"/"+file_name))
    return information