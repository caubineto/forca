# Matriz inicial
row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]

# Função para imprimir o mapa
def print_map(map):
    for row in map:
        print(" ".join(row))

# Função para marcar um ponto com um arquivo .X
def mark_point(map, x, y):
    if 0 <= x < 3 and 0 <= y < 3:
        if map[y][x] != "X":
            map[y][x] = "X"
        else:
            print("Você já marcou este ponto com um X.")
    else:
        print("Coordenadas inválidas. Fora do alcance do mapa.")

# Imprimir o mapa inicial
print("Mapa inicial:")
print_map(map)

# Obter as coordenadas do usuário
while True:
    try:
        x = int(input("Informe a coordenada X (0, 1 ou 2): "))
        y = int(input("Informe a coordenada Y (0, 1 ou 2): "))
        mark_point(map, x, y)
        print("Mapa atualizado:")
        print_map(map)
    except ValueError:
        print("Por favor, insira um número válido.")
