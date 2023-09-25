#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
leng=int(input("Enter total length of password:"))
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
nr_complexity=input(f"How about complexity(easy or hard):")
nr_complexity=nr_complexity.lower()
tot=nr_letters+nr_symbols+nr_numbers
if leng==tot:
 if nr_complexity=="easy":
#Eazy Level
  password = ""

  for char in range(1, nr_letters + 1):
    password += random.choice(letters)

  for char in range(1, nr_symbols + 1):
   password += random.choice(symbols)

  for char in range(1, nr_numbers + 1):
   password += random.choice(numbers)

  print(f"Your password is: {password}")
 elif nr_complexity=="hard":
#Hard Level
  password_list = []

  for char in range(1, nr_letters + 1):
   password_list.append(random.choice(letters))

  for char in range(1, nr_symbols + 1):
   password_list += random.choice(symbols)

  for char in range(1, nr_numbers + 1):
   password_list += random.choice(numbers)

  random.shuffle(password_list)


  password = ""
  for char in password_list:
   password += char

  random.shuffle(password_list)


  print(f"Your password is: {password}")
 else:
  print("Enter proper complexity")
else:
    print("Count doesn't match")