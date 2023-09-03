import random

# Split string method
names_string = input("Dê-me os nomes de todos, separados por vírgula.\n")
names = names_string.split(", ")

numItens = (len(names))
randomChoise = random.randint(0, numItens - 1)
pessoaQuevaiPagar = names[randomChoise]
print(pessoaQuevaiPagar + ' vai pagar a refeição hoje!')