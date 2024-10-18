import os
import requests
clear = lambda: os.system('cls')

#Functions
def SaveData(category):
  page = 1
  dataList = []
  while True:
    url = f'https://swapi.dev/api/{category}/?page={page}'
    response = requests.get(url)
    data = response.json()
    clear()
    print(f'>>>Downloading {category} data: page {page}')
    dataList.extend(data['results'])
    if (data['next'] is None):
      break
    page += 1
  return dataList

def ParseInfo(person, info):
    try:
        return float(person[info].replace(',', ''))
    except ValueError:
        return float('-inf')

def GetTop(dataList, num, info, metric):
   for index, data in enumerate(dataList[:num], start=1):
      print(f'{index}- {data['name']}: {data[info]} {metric}')


#Script
people = SaveData('people')
vehicles = SaveData('vehicles')

while True:
  clear()
  action = input(
'''--Wellcome to the SWAPI script--
>Which category do you want to check?
  1-People
  2-Vehicles
  0-Exit
''')
  match action:
    case '1':
      clear()
      action = input(
'''>What do you want to know?
  1-Who is the heaviest?
  2-Who is the tallest?
  3-Wich characters have appeared in most films?
  4-Wich planets have the largest number of characters?
''')
      match action:
        case '1':
            clear()
            peopleByMass = sorted(people, key=lambda person: ParseInfo(person, 'mass'), reverse=True)
            print('---Top 5 heaviest star wars characters---')
            GetTop(peopleByMass, 5, 'mass', 'Kg')
            action = input('\n>Return')
        case '2':
            clear()
            peopleByHeight = sorted(people, key=lambda person: ParseInfo(person, 'height'), reverse=True)
            print('---Top 5 tallest star wars characters---')
            GetTop(peopleByHeight, 5, 'height', 'Cm')
            action = input('\n>Return')
        case '3':
            clear()
            print('WIP')
            action = input('\n>Return')
        case '4':
            clear()
            print('WIP')
            action = input('\n>Return')
        case _:
            clear()
            print('Invalid option. Please choose a valid number')
            action = input('\n>Return')
    case '2':
        clear()
        action = input(
'''>What do you want to know?
  1-Which vehicle is the most expensive?
  2-Which vehicle is the largest?
  3-Which vehicle is the fastest?
  4-Wich vehicles have appeared in most films?
''')
        match action:
          case '1':
              clear()
              print('WIP')
              action = input('\n>Return')
          case '2':
              clear()
              print('WIP')
              action = input('\n>Return')
          case '3':
              clear()
              print('WIP')
              action = input('\n>Return')
          case '4':
              clear()
              print('WIP')
              action = input('\n>Return')
          case _:
              clear()
              print('Invalid option. Please choose a valid number')
              action = input('\n>Return')
    case '0':
        break
    case _:
      clear()
      print('Invalid option. Please choose a valid number')
      action = input('\n>Return')