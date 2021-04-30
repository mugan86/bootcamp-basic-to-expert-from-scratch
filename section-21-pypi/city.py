API_KEY = '194f66064a427d3f0bcca212ab703736'
URL = 'https://api.openweathermap.org/data/2.5/'

import requests
"""

weather?
lat=24.9518041&lon=-104.7457739
q=Bilbao
&appid=
&lang=es&units=metric
"""

# POr ciudad
bilbao = f'{URL}weather?q=Bilbao&lang=es&units=metric&appid={API_KEY}'
print(bilbao)
r = requests.get(bilbao)

print(r.status_code)
print(r.json())
print('===============================')
# Coordenadas geográficas
durango_mx = f'{URL}weather?lat=24.9518041&lon=-104.7457739&lang=es&units=metric&appid={API_KEY}'
print(durango_mx)
r = requests.get(durango_mx)

print(r.status_code)
print(r.json())
print('===============================')
# Coordenadas geográficas (Txindoki)
txindoki = f'{URL}weather?lat=43.0227616&lon=-2.0901526&lang=es&units=metric&appid={API_KEY}'
print(txindoki)
r = requests.get(txindoki)

print(r.status_code)
print(r.json())