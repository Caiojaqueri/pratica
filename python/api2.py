# consumo de API de uma forma melhorada 

import requests 

def fetch_data(endpoint):
    response = requests.get('https://rickandmortyapi.com/api/character')

    if response.status_code == 200:
        return response.json()
    else:
        return None

characters = fetch_data('character')

if characters:
    print(characters)
else:
    print("Erro na requisição")