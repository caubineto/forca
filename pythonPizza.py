print("Bem-vindo ao Python Pizza Delivery!")
size = input("Que tamanho de pizza você quer? S, M ou L: ")
add_pepperoni = input("Você quer pepperoni? Y ou N: ")
extra_cheese = input("Você quer queijo extra? Y ou N: ")
price = 0

if size == 'S':
    price += 15
    if add_pepperoni == 'Y':
        price += 2
    if extra_cheese == 'Y':
        price += 1
    print (f'Sua conta final é: R${price},00.')
elif size == 'M':
    price += 20
    if add_pepperoni == 'Y':
        price += 3
    if extra_cheese == 'Y':
        price += 1
    print (f'Sua conta final é: R${price},00.')
elif size == 'L':
    price += 25
    if add_pepperoni == 'Y':
        price += 3
    if extra_cheese == 'Y':
        price += 1
    print (f'Sua conta final é: R${price},00.')

else:
    print('you dont never come here.')