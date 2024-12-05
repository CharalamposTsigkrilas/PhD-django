import requests
# TOKEN = 'Token 934ef7f1007d5fb83dd7477b905e53741e155552'
# URL = 'http://localhost:30082/api/staff'
# headers={ 'Authorization' : TOKEN }
# res = requests.get(URL,headers=headers)
# print(res.text)

URL = 'https://mydep.ditapps.hua.gr/api/course'
token = 'e009d050d7e7248c7c2f9945287b4f9487e4b6ce'
headers={'Authorization' : 'Token ' + token}
payload = {'id' : 331}
res = requests.get(URL,headers = headers, params = payload)
print(res.text)




