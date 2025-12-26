import requests 

response = requests.get('https://rickandmortyapi.com/api')

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Erro na requisição: ", response.status_code)