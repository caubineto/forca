print('''
 *******************************************************************************
           |                   |                  |                     |
  _________|________________.=""_;=.______________|_____________________|_______
 |                   |  ,-"_,=""     `"=.|                  |
 |___________________|__"=._o`"-._        `"=.______________|___________________
           |                `"=._o`"=._      _`"=._                     |
  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
 |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
 |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
 |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
 |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
 ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
 /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
 ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
 /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
 ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
 /______/______/______/______/______/______/______/______/______/______/_____ /
 *******************************************************************************
 ''')
print("Bem vindo a Ilha do Tesouro!")
print("Sua missão é achar o baú do tesouro!") 

escolha1 = input('Você está em uma encruzilhada. Para onde você quer ir? "Direita" ou "Esquerda" \n').lower()
if escolha1 == 'esquerda':
    escolha2 = input('Você chegou a um lago. Há uma ilha no meio do lago. Digite "esperar" para aguardar um barco. Digite "nadar" para nadar. \n').lower()
    if escolha2 == 'esperar':
        escolha3 = input('Você chega à ilha ileso. Há uma casa com 3 portas. Um vermelho, um amarelo e um azul. Qual cor você escolhe? \n').lower()
        if escolha3 == 'vermelho':
            print('É uma sala cheia de fogo. Game Over.')
        elif escolha3 == 'amarelo':
            print('Você achou o tesouro. Você ganhou!')
        elif escolha3 == 'azul':
            print('Você entra em uma sala de feras. Game Over')
        else:
            print('Essa porta não existe. Game Over.')
    else:
        print('Você é atacado por uma truta furiosa. Game Over.')
else:
    print('Você caiu em um buraco. Game Over.')