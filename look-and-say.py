line = input("Give the first line: ")
repeats = input("How many lines do i generate? ")
lineCount = 0
print(f'>{line}')
while lineCount < int(repeats):
  newline = oldchar = ''
  chars = counters = []
  for char in line:
    if char != oldchar:
      chars.append(char)
      counters.append(1)
    else:
      counters[-1] = counters[-1] + 1
    oldchar = char
  for i, char in enumerate(chars):
    newline += str(counters[i]) + char
  print(newline)
  line = newline
  lineCount += 1