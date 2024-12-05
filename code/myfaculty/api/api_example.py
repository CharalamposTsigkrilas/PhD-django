import requests
# TOKEN = 'Token 934ef7f1007d5fb83dd7477b905e53741e155552'
# URL = 'http://localhost:30082/api/staff'
# headers={ 'Authorization' : TOKEN }
# res = requests.get(URL,headers=headers)
# print(res.text)

URL = 'http://localhost:30082/api/auth/'
data = {'username' : 'admin',
        'password' : 'hua123##'}
response = requests.post(URL, data = data)
reponse_json = response.json()
token = reponse_json['token']

URL = 'http://localhost:30082/api/staff'
headers={'Authorization' : 'Token ' + token}
payload={'email' : 'thkam@hua.gr'}
res = requests.get(URL,headers = headers, params = payload)
print(res.text)

URL = 'http://localhost:30082/api/associates'
headers={'Authorization' : 'Token ' + token}
payload = {'card_no' : '04c64302167480'}
res = requests.get(URL,headers = headers, params = payload)
print(res.text)



