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

def ParseInfo(data, info):
    try:
        return float(data[info].replace(',', ''))
    except ValueError:
        return float('-inf')

def SortByInfo(dataList, info):
    sortedList = sorted(dataList, key=lambda data: ParseInfo(data, info), reverse=True)
    return sortedList

def SortByFilms(dataList):
  numberOfFilms = list(map(lambda data: {"name": data["name"], "films": len(data["films"])}, dataList))
  sortedList = sorted(numberOfFilms, key=lambda data: data['films'], reverse=True)
  return sortedList

def GetTop(dataList, num, info, metric):
   for index, data in enumerate(dataList[:num], start=1):
      print(f'  {index}- {data['name']}: {data[info]} {metric}')

def WellcomeMenu():
  clear()
  action = input(
'''--Wellcome to the SWAPI script--
>Which category do you want to check?
  1-People
  2-Vehicles
  0-Exit
''')
  match action:
    case '0':
      return -1
    case '1':
      PeopleMenu()
      return 1
    case '2':
      VehiclesMenu()
      return 2
    case _:
      clear()
      print('Invalid option. Please choose a valid number')
      action = input('\n>Return')

def PeopleMenu():
  clear()
  action = input(
'''>What do you want to know?
  1-Who is the heaviest?
  2-Who is the tallest?
  3-Wich characters have appeared in most films?
  4-Wich planets have the largest number of characters?
  0-Return
''')
  match action:
    case '0':
        return 0
    case '1':
      clear()
      peopleByMass = SortByInfo(people, 'mass')
      print('---Top 5 heaviest Star Wars characters---')
      GetTop(peopleByMass, 5, 'mass', 'Kg')
      action = input('\n>Return')
      return 1
    case '2':
      clear()
      peopleByHeight = SortByInfo(people, 'height')
      print('---Top 5 tallest Star Wars characters---')
      GetTop(peopleByHeight, 5, 'height', 'Cm')
      action = input('\n>Return')
      return 1
    case '3':
      clear()
      print('---Top 5 Star Wars characters who have appeared in the most films---')
      peopleByFilms = SortByFilms(people)
      GetTop(peopleByFilms, 5, 'films', 'films')
      action = input('\n>Return')
      return 1
    case '4':
      clear()
      print('WIP')
      action = input('\n>Return')
      return 1
    case _:
      clear()
      print('Invalid option. Please choose a valid number')
      action = input('\n>Return')
      return 1

def VehiclesMenu():
  clear()
  action = input(
'''>What do you want to know?
  1-Which vehicle is the most expensive?
  2-Which vehicle is the largest?
  3-Which vehicle is the fastest?
  4-Wich vehicles have appeared in most films?
  0-Return
''')
  match action:
    case '0':
      return 0
    case '1':
      clear()
      vehiclesByCost = SortByInfo(vehicles, 'cost_in_credits')
      print('---Top 5 most expensive Star Wars vehicles---')
      GetTop(vehiclesByCost, 5, 'cost_in_credits', 'Credits')
      action = input('\n>Return')
      return 2
    case '2':
      clear()
      vehiclesByLength = SortByInfo(vehicles, 'length')
      print('---Top 5 largest Star Wars vehicles---')
      GetTop(vehiclesByLength, 5, 'length', 'm')
      action = input('\n>Return')
      return 2
    case '3':
      clear()
      vehiclesBySpeed = SortByInfo(vehicles, 'max_atmosphering_speed')
      print('---Top 5 fastest Star Wars vehicles---')
      GetTop(vehiclesBySpeed, 5, 'max_atmosphering_speed', 'Km/h')
      action = input('\n>Return')
      return 2
    case '4':
      clear()
      print('---Top 5 Star Wars vehicles that have appeared in the most films---')
      vehiclesByFilms = SortByFilms(vehicles)
      GetTop(vehiclesByFilms, 5, 'films', 'films')
      action = input('\n>Return')
      return 2
    case _:
      clear()
      print('Invalid option. Please choose a valid number')
      action = input('\n>Return')
      return 2

#Script
people = SaveData('people')
vehicles = SaveData('vehicles')
activeMenu = 0

while True:
  match activeMenu:
    case 0:  
      activeMenu = WellcomeMenu()
    case 1:
      activeMenu = PeopleMenu()
    case 2:
      activeMenu = VehiclesMenu()
    case _:
      break