import json
from turtle import delay
import requests
import msvcrt



# En este caso hacemos la solicitud para el caso de consulta de ciertos indicadores
url = f'https://mindicador.cl/api'
response = requests.get(url)
data = json.loads(response.text.encode("utf-8"))
# Para que el json se vea ordenado, retornar pretty_json
pretty_json = json.dumps(data, indent=2)
print(pretty_json)
print('Valor Dolar: $',data['dolar']['valor'])
print('Valor Euro: $',data['euro']['valor'])
print('Valor IPC: $',data['ipc']['valor'])
print('Valor UF: $',data['uf']['valor'])
print('Valor UTM: $',data['utm']['valor'])
print('Valor bitcoin: $',data['bitcoin']['valor'])

msvcrt.getch()


