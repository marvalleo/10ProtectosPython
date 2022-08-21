import json
import requests
import msvcrt

# En este caso hacemos la solicitud para el caso de consulta de ciertos indicadores
ufUrl = 'https://api.cmfchile.cl/api-sbifv3/recursos_api/uf?apikey=ed9a563e5054dc6a2901e56530e16a985d01fada&formato=json'
ufResponse = requests.get(ufUrl)
ufData = json.loads(ufResponse.text.encode("utf-8"))
ufRespuesta = ufData['UFs'][0]['Valor']

# dolarUrl = 'https://api.cmfchile.cl/api-sbifv3/recursos_api/dolar/2022/08/dias/19?apikey=ed9a563e5054dc6a2901e56530e16a985d01fada&formato=json'
dolarUrl = 'https://api.cmfchile.cl/api-sbifv3/recursos_api/dolar/?apikey=ed9a563e5054dc6a2901e56530e16a985d01fada&formato=json'
dolarResponse = requests.get(dolarUrl)
if dolarResponse.status_code == 200:
    dolarData = json.loads(dolarResponse.text.encode("utf-8"))
    dolarRespuesta = dolarData['Dolares'][0]['Valor']
else:
    url = "https://api.apilayer.com/currency_data/convert?to=CLP&from=USD&amount=1"
    payload = {}
    headers= {
    "apikey": "UCAXWzbr9OpnbVouDuPpHHpAFHkbKcy2"
    }
    response = requests.request("GET", url, headers=headers, data = payload)
    dolarData = json.loads(response.text.encode("utf-8"))
    dolarRespuesta = dolarData['result']
# Para que el json se vea ordenado, retornar pretty_json
pretty_json = json.dumps(ufData, indent=2)
pretty_json2 = json.dumps(dolarData, indent=2)
# print('PrettyJson1: ', pretty_json)
# print('PrettyJson2: ', pretty_json2)

print('Valor UF: $',ufRespuesta)
print('Valor Dolar: $',dolarRespuesta)


msvcrt.getch()