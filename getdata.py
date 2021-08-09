import requests

get_url = 'http://127.0.0.1:8000/api/student_info/1'

d=requests.get(url=get_url)                             
data = d.json()
print(data)

