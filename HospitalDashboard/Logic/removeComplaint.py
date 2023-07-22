

def remove(token,complaints):
    print(token,"Cool")
    for index,complaint in enumerate(complaints):
        if(complaint['token']==str(token)):
            complaints.pop(index)
            break
    return complaints