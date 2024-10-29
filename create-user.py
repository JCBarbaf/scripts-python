import os
clear = lambda: os.system('cls')
import re
import getpass
import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import bcrypt

BAD = "\033[31m"
GOOD = "\033[32m"
RESET = "\033[0m"

load_dotenv()

email_rgx = r'^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$'
password_rgx = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[!?\-.$%&@#])[A-Za-z\d!?\-.$%&@#]{8,}$'

def create_connection():
  connection = None
  try:
    connection = mysql.connector.connect(
      host= os.getenv('DB_HOST'),
      user= os.getenv('DB_USER'),
      password= os.getenv('DB_PASSWORD'),
      database= os.getenv('DB_NAME')
    )
    # print(GOOD + 'Connection to MySQL DB successful' + RESET)
  except Error as e:
    print(BAD + f'Connection error: {e}' + RESET)
  return connection


while True:
  clear()
  print('>>> User creation script')
  username = input('Username (email): \n')
  if (not re.match(email_rgx, username)):
    clear()
    input(BAD + 'Please introduce a valid username' + RESET)
    continue
  password = getpass.getpass('Password: \n')
  if (not re.match(password_rgx, password)):
    clear()
    input(BAD + 'Please introduce a valid password \nAt least 8 characters, one uppercase, one lowercase, one number and one special character' + RESET)
    continue
  repeat_pswd = getpass.getpass('Repeat password: \n')
  if (password != repeat_pswd):
    clear()
    input(BAD + 'The passwords do not match' + RESET)
    continue
  break

salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
conn = create_connection()
query = 'INSERT INTO users (name, password) VALUES (%s, %s)'
if conn:
  cursor = conn.cursor()
  try:
      cursor.execute(query, (username, hashed_password))
      conn.commit()
      user_id = cursor.lastrowid
      clear()
      print(GOOD + f'User created with id: {user_id}' + RESET)
  except Error as e:
      clear()
      print(BAD + f'Error creating user: {e}' + RESET)
  finally:
      cursor.close()
  conn.close()
