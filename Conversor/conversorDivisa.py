
import msvcrt
import re
import string
import requests

monto = input("Introduce el monto CLP -> USD: ")

url = "https://api.apilayer.com/currency_data/convert?to=CLP&from=USD&amount={}".format(monto)

payload = {}
headers= {
  "apikey": "UCAXWzbr9OpnbVouDuPpHHpAFHkbKcy2"
}

response = requests.request("GET", url, headers=headers, data = payload)

status_code = response.status_code
result = response.text
found = result[205:215]
#print(result)
print("Cantidad en dolares: $",found)


msvcrt.getch()