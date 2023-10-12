import random
import os
from listaPalavras import listadePalavras  # Importa a lista de palavras do arquivo listaPalavras.py
from forcaArt import etapas, logo  # Importa a arte do jogo e as etapas do arquivo forcaArt.py

print(logo)

# Escolhe uma palavra aleatória da lista de palavras
palavraEscolhida = random.choice(listadePalavras)
vidas = 6

display = []  # Inicializa uma lista para exibir as letras da palavra escondida
for letra in range(len(palavraEscolhida)):
    display += '_'  # Preenche a lista com '_'
print(display)

fimDoJogo = False  # Inicializa a variável que controla o término do jogo
while not fimDoJogo:
    palpite = input(f'Escolha uma letra: ').lower()  # Solicita ao jogador que escolha uma letra e a converte para minúsculas

    for posicao in range(len(palavraEscolhida)):
        letra = palavraEscolhida[posicao]
        # Verifica se a letra do palpite corresponde à letra na palavra escolhida e atualiza a lista de exibição
        if letra == palpite:
            display[posicao] = letra

    if palpite not in palavraEscolhida:
        vidas -= 1
        if vidas == 0:
            fimDoJogo = True
            os.system('cls')  # Limpa a tela (funciona no Windows)
            print(f'Você Perdeu!')
            print(f'A palavra era: {palavraEscolhida}')

    print(display)  # Exibe a lista de exibição atual

    # Verifica se não há mais '_' na lista de exibição, o que significa que o jogador venceu
    if "_" not in display:
        fimDoJogo = True
        os.system('cls')  # Limpa a tela (funciona no Windows)
        print(f'A palavra era: {palavraEscolhida}')
        print(f'Você venceu!')

    print(etapas[vidas])  # Exibe a arte correspondente ao número de vidas restantes
