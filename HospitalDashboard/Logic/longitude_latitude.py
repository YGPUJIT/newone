from urllib import request,parse
import urllib
import json



def get_lon_lat(city,area,pincode,country="India"):
    if(city.upper()=="bengaluru".upper()):
        city="Bangalore"
    value={
        'key':"pk.1d6b282ce26796c6c4af35531121dfd8",
        'street':area.strip().upper(),
        'city':city,
        'state':'KARNATAKA',
        'country':country,
        'postalcode':pincode.strip(),
        'format':'json'
    }
    try:
        url="https://us1.locationiq.com/v1/search.php?"+parse.urlencode(value)
        print(url)
        value=request.urlopen(url)
        value=json.loads(value.read().decode('utf-8'))[0]
        print('Logitude and latitude')
        return {'longitude':value.get('lon',0.00000),'latitude':value.get('lat',0.00000)}
    except:
        print('Logitude and latitude false')
        return {'longitude':0.00000,'latitude':0.00000}

# print(get_lon_lat("bengaluru","jay","560058"))
