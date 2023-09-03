import random

pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

papel = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

maos = [pedra, papel, tesoura]

escolhaUsuario = int(input("Qual você escolhe? Digite 0 para Pedra, 1 para Papel ou 2 para Tesoura.\n"))
print(maos[escolhaUsuario])

escolhaPC = random.randint(0, 2)
print('O computador escolheu:')
print(maos[escolhaPC])

if escolhaUsuario >= 3 or escolhaUsuario < 0:
    print('Você digitou um número inválido, você perdeu!')
elif escolhaUsuario == 0 and escolhaPC == 2:
    print('Voce venceu! Parabéns!')
elif escolhaUsuario == 1 and escolhaPC == 0:
    print ('Você venceu! Parabéns!')
elif escolhaUsuario == 2 and escolhaPC == 1:
    print ('Você venceu! Parabéns!')
elif escolhaUsuario == escolhaPC:
    print('Empate!')
else:
    print('Você perdeu, tente novamente!')