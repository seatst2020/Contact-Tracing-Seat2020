import requests

global response

def generate(criteria):
  try:
    response = requests.get('https://randomuser.me/api/?inc=name')
    return response.json()['results'][0]['name'][criteria] 
  except:
    print('An error occured contacting API')

