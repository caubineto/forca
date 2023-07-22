print('Welcome to the tipCalculator!')

total = float(input('What was the total bill? R$'))
gorjeta = int(input('What porcentage tip would you like to give? 10, 12 or 15? '))
pessoas = int(input('How many people to split the bill? '))

gorjetaPorcentagem = gorjeta / 100
valorTotalGorjeta = total * gorjetaPorcentagem
contaTotal = total + valorTotalGorjeta
gorjetaPessoas = contaTotal / pessoas
valorFinal = round(gorjetaPessoas, 2)

print(f'Each person should pay R$ {valorFinal} ' )