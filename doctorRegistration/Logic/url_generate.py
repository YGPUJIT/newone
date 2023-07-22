


def generate(code,hid):
    url="http://localhost:8000/doctor/registrationConfirmation/"+hid+code
    print(url)
    return url