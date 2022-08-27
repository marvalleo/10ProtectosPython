
<<<<<<< HEAD
import json
=======
import msvcrt
import re
import string
>>>>>>> 840895b5b7ba8dc39f9b397cb8f4ffbf6b880d74
import requests

# monto = input("Introduce el monto CLP -> USD: ")

#url = "https://api.apilayer.com/currency_data/convert?to=CLP&from=USD&amount={}".format(monto)
url = "https://api.apilayer.com/currency_data/convert?to=CLP&from=USD&amount=1"

payload = {}
headers= {
  "apikey": "UCAXWzbr9OpnbVouDuPpHHpAFHkbKcy2"
}

response = requests.request("GET", url, headers=headers, data = payload)
data = json.loads(response.text.encode("utf-8"))

status_code = response.status_code
result = response.text

found = result[205:215]
#print(result)
print("Cantidad en dolares 1: $",found)
print("Cantidad en dolares 2: $",data['result'])

msvcrt.getch()