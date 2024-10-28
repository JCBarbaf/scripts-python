import re

print(">>>Welcome to find in file")
file_url = input("Witch file do I search? ")
string_to_find = input("What do you want me to look for? ")
case_sensitive = input("Do you want me to be case sensitive? (y/N): ").lower() == "y"

file = open(file_url, "r")
if (case_sensitive):
  file_text = file.read()
else:
  file_text = file.read().lower()
  string_to_find = string_to_find.lower()

instances = len(re.findall(string_to_find, file_text))
print(f'In the selected file the string "{string_to_find}" appears {instances} times')
