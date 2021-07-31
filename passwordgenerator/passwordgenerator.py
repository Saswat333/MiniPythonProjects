import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
           'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


# the sequence of password is constant first letter,then symbol then number but within seach set it will be random eg: defg!#345
def passwordGeneratorEasy():
    password1 = ""
    for char in range(1,nr_letters+1):
        password1 += random.choice(letters)
    for symb in range(1, nr_symbols+1):
        password1 += random.choice(symbols)
    for num in range(1, nr_numbers + 1):
        password1 += random.choice(numbers)
    print( f"Easy password {password1}")


# each character is random eg: g$56hj2#

def passwordGeneratorHard():
    password2 = []
    password2_string = ""
    for char in range(1, nr_letters + 1):
        password2.append(random.choice(letters))
    for symb in range(1, nr_symbols + 1):
        password2 += random.choice(symbols)
    for num in range(1, nr_numbers + 1):
        password2 += random.choice(numbers)
    random.shuffle(password2)
    for char in password2:
        password2_string += char

    print(f"Hard is {password2_string}")



print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
print("Suggested password are: ")
passwordGeneratorEasy()
passwordGeneratorHard()