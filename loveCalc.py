print("Bem vindos a Calculadora do Amor!")
name1 = input("Qual o seu nome? \n")
name2 = input("Qual é o nome dele(a)? \n")

combineded_Stings = name1 + name2
strings_Baixas = combineded_Stings.lower()

t = strings_Baixas.count('t')
r = strings_Baixas.count('r')
u = strings_Baixas.count('u')
e = strings_Baixas.count('e')
true = t + r + u + e

l = strings_Baixas.count('l')
o = strings_Baixas.count('o')
v = strings_Baixas.count('v')
e = strings_Baixas.count('e')
love = l + o + v + e

tl = int(str(true) + str(love))

if (tl < 10) or (tl > 90):
    print(f'Sua pontuação é {tl}%, você vai junto como coca e mentos.')
elif (tl <= 50) or (tl >= 40):
    print(f'Sua pontuação é {tl}%, vocês estão bem juntos.')
else:
    print(f'Sua pontuação é {tl}%')
