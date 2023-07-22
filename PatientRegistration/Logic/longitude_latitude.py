from urllib import request,parse
import json



def get_lon_lat(city,area,pincode,country="India"):
    if(city.upper()=="Bengaluru".upper()):
        city='Bangalore'.upper()
    value={
        'key':"pk.1d6b282ce26796c6c4af35531121dfd8",
        'street':area.lower().strip(),
        'city':city,
        'state':'karnataka',
        'country':country,
        'postalcode':pincode,
        'format':'json'
    }
    try:
        url="https://eu1.locationiq.com/v1/search.php?"+parse.urlencode(value)
        value=request.urlopen(url)
        print("HERE")
        value=json.loads(value.read().decode('utf-8'))[0]
        return {'longitude':value.get('lon',0.00000),'latitude':value.get('lat',0.00000)}
    except:
        return {'longitude':0.00000,'latitude':0.00000}

# print(get_lon_lat("bengaluru","jay","560058"))
