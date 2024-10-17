import os
import requests
clear = lambda: os.system('cls')

page = 1
people = []
while True:
  url = f'https://swapi.dev/api/people/?page={page}'
  response = requests.get(url)
  data = response.json()
  clear()
  print(f'>>>Downloading data: page {page}')
  people.extend(data['results'])
  if (data['next'] is None):
    break
  page += 1
def parse_mass(person):
    try:
        return float(person['mass'].replace(',', ''))
    except ValueError:
        return float('-inf')
peopleByMass = sorted(people, key=parse_mass, reverse=True)
clear()
print('---Top 5 heaviest star wars characters---')
for person in peopleByMass[:5]:
  print(f'{person['name']}: {person['mass']} Kg')