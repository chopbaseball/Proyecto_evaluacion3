import requests


response = requests.get('https://dbd-api.herokuapp.com/perks').json()



print(response)