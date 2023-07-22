
def check(model,hid,password):
    print(model)
    model_password=model.password
    print(model_password)
    if(model_password.strip()!=password):
        return False
    return True