import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Bem-vindo ao Gerador PyPassword!")
nr_letters= int(input(f"Quantas letras você gostaria em sua senha?\n")) 
nr_symbols = int(input(f"Quantos símbolos você gostaria?\n"))
nr_numbers = int(input(f"Quantos números você gostaria?\n"))


senha_lista = []

for carac in range(1, nr_letters + 1):
    senha_lista.append(random.choice(letters))

for carac in range(1, nr_symbols + 1):
    senha_lista += random.choice(symbols)

for carac in range(1, nr_numbers + 1):
    senha_lista += random.choice(numbers)

random.shuffle(senha_lista)

senha = ''
for carac in senha_lista:
    senha += carac

print(f'Sua senha é {senha}')