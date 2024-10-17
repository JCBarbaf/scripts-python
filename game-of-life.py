import os
import time
import random
clear = lambda: os.system('cls')
rows = cols = 13
petriDish = [[0 for _ in range(cols)] for _ in range(rows)]
livingCellsNum = random.randint(35, 45)
positions = [(i, j) for i in range(rows) for j in range(cols)]
selected_positions = random.sample(positions, livingCellsNum)
for pos in selected_positions:
    petriDish[pos[0]][pos[1]] = 1

cellAge = [[0 for _ in range(cols)] for _ in range(rows)]

DEAD = "\033[31m"
ALIVE = "\033[32m"
RESET = "\033[0m"

counter = 1
print(all(cell == 0 for row in petriDish for cell in row))
while True:
  clear()
  print(f'Generations: {counter}')
  
  newPetriDish = [[0 for _ in range(len(petriDish[0]))] for _ in range(len(petriDish))]

  for i in range(len(petriDish)):
      for j in range(len(petriDish[i])):
          livingNeighbors = 0
          
          for x in range(-1, 2):
              for y in range(-1, 2):
                  if (x == 0 and y == 0):
                      continue
                  ni, nj = i + x, j + y
                  if 0 <= ni < len(petriDish) and 0 <= nj < len(petriDish[i]) and petriDish[ni][nj] == 1:
                      livingNeighbors += 1

          if petriDish[i][j] == 1:
              if livingNeighbors < 2 or livingNeighbors > 3:
                  newPetriDish[i][j] = 0
                  cellAge[i][j] = 0
              else:
                  newPetriDish[i][j] = 1
                  cellAge[i][j] += 1
          else:
              if livingNeighbors == 3:
                  newPetriDish[i][j] = 1
                  cellAge[i][j] += 1
          if cellAge[i][j] >= 10:
            newPetriDish[i][j] = 0
            cellAge[i][j] = 0
  petriDish = newPetriDish

  for row in petriDish:
      printRow = ''
      for cell in row:
          if cell == 1:
            print(ALIVE + "1" + RESET, end=' ')
          else:
            print(DEAD + "0" + RESET, end=' ')
      print(printRow)

  if all(cell == 0 for row in petriDish for cell in row):
      break

  counter += 1
  time.sleep(1)