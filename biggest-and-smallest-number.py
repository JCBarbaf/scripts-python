#Functions
def GetNumber():
  while ('true'):
    num = input('Give me a number or press 0 to exit:')
    if num.isnumeric():
      return num
    else:
      print('Thats not a valid number, try again')

#Code
nums = []
while ('true'):
  num = GetNumber()
  if int(num) != 0:
    nums.append(float(num))
  else:
    break
print(f'The biggest number you gave me was {max(nums)} and the smallest number was {min(nums)}')