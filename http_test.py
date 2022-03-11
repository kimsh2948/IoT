import requests, json

url='http://192.168.0.6:8000/'
headers = {'Content-Type': 'application/json; charset=utf-8'}

class Http:
    def response(self, value):
        params = {'value': value}
        res = requests.post(url=url, data=json.dumps(params), headers=headers)
        print(res.text)






