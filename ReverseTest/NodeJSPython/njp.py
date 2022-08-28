from urllib import request, response
import requests

data={
	'name': 'ղķ˹',
    'image': 'harden.png',
    'birthday': '1989-08-26',
    'height': '196cm',
    'weight': '99.8KG'
}
url='http://localhost:3000'
response=requests.post(url,json=data)
print(response.text)




