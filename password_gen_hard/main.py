#Password Generator Project
import random
import objects

# print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password = []

for amount_letters in range(nr_letters):
    password += (random.choice(objects.letters))

for amount_symbols in range(nr_symbols):
    password += (random.choice(objects.symbols))

for amount_numbers in range(nr_numbers):
    password += random.choice(objects.numbers)
    
# ---------------------

random.shuffle(password)
generated_pw = ""
for values in password:
    generated_pw += values
print(f"Your generated password is: {generated_pw}")