import requests
import json
post_url = 'http://127.0.0.1:8000/api/student_create'

item = {
    'name':'fate',
    'roll':23,
    'city':'uttara'
}

json_data = json.dumps(item)                        # convert dict to json

r = requests.post(url=post_url, data=json_data)     # response come and store in r

data = r.json()                                 

print(data)