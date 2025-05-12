import heapq
import math
import random

# -------------------------- Funções Utilitárias --------------------------

def encontrar_pontos(labirinto):
    """
    Encontra as coordenadas do ponto de início ('S') e fim ('E') no labirinto.
    Valida se há exatamente um 'S' e um 'E'.
    """
    inicio = fim = None
    for i, linha in enumerate(labirinto):
        for j, valor in enumerate(linha):
            if valor == 'S':
                if inicio is not None:
                    raise ValueError("Erro: múltiplos pontos de início encontrados.")
                inicio = (i, j)
            elif valor == 'E':
                if fim is not None:
                    raise ValueError("Erro: múltiplos pontos de fim encontrados.")
                fim = (i, j)
    if inicio is None or fim is None:
        raise ValueError("Erro: o labirinto deve conter exatamente um 'S' e um 'E'.")
    return inicio, fim

def heuristica(a, b):
    """
    Distância de Manhattan entre dois pontos (a, b).
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def custo_celula(valor):
    """
    Define o custo para andar sobre determinada célula.
    Pode ser expandido para terrenos com diferentes pesos.
    """
    if valor in ('0', 'S', 'E'):
        return 1    # Caminho livre ou início/fim
    elif valor == '2':
        return 5    # Terreno mais difícil (exemplo)
    else:
        return math.inf    # Obstáculo

def gerar_labirinto(linhas, colunas, probabilidade_obstaculo=0.3):
    """
    Gera um labirinto 2D aleatório.
    """
    labirinto = [['0' for _ in range(colunas)] for _ in range(linhas)]

    # Coloca obstáculos aleatoriamente
    for i in range(linhas):
        for j in range(colunas):
            if random.random() < probabilidade_obstaculo:
                labirinto[i][j] = '1'

    # Garante que os pontos de início e fim estejam em locais diferentes e livres
    while True:
        inicio_x = random.randrange(linhas)
        inicio_y = random.randrange(colunas)
        fim_x = random.randrange(linhas)
        fim_y = random.randrange(colunas)
        if (inicio_x, inicio_y) != (fim_x, fim_y) and labirinto[inicio_x][inicio_y] == '0' and labirinto[fim_x][fim_y] == '0':
            labirinto[inicio_x][inicio_y] = 'S'
            labirinto[fim_x][fim_y] = 'E'
            break
        # Se os pontos coincidirem ou caírem em obstáculos, tenta novamente

    return labirinto

# -------------------------- Algoritmo A* --------------------------

def a_star(labirinto, inicio, fim, permitir_diagonais=False):
    """
    Algoritmo A* para encontrar o menor caminho de 'inicio' até 'fim'.
    Permite diagonais opcionalmente.
    """
    movimentos = [(-1,0), (1,0), (0,-1), (0,1)]
    if permitir_diagonais:
        movimentos += [(-1,-1), (-1,1), (1,-1), (1,1)]

    heap = []
    heapq.heappush(heap, (0, inicio))
    veio_de = {}
    custo_ate = {inicio: 0}

    while heap:
        _, atual = heapq.heappop(heap)

        if atual == fim:
            # Reconstrói o caminho
            caminho = []
            while atual in veio_de:
                caminho.append(atual)
                atual = veio_de[atual]
            caminho.append(inicio)
            return caminho[::-1]

        for dx, dy in movimentos:
            x, y = atual[0] + dx, atual[1] + dy
            if 0 <= x < len(labirinto) and 0 <= y < len(labirinto[0]):
                valor = labirinto[x][y]
                custo_terreno = custo_celula(valor)
                if custo_terreno == math.inf:
                    continue

                movimento_diagonal = abs(dx) + abs(dy) == 2
                fator_diagonal = math.sqrt(2) if movimento_diagonal else 1
                novo_custo = custo_ate[atual] + custo_terreno * fator_diagonal

                vizinho = (x, y)
                if vizinho not in custo_ate or novo_custo < custo_ate[vizinho]:
                    custo_ate[vizinho] = novo_custo
                    prioridade = novo_custo + heuristica(vizinho, fim)
                    heapq.heappush(heap, (prioridade, vizinho))
                    veio_de[vizinho] = atual

    return None  # Sem solução

# -------------------------- Impressão --------------------------

def imprimir_labirinto_com_caminho(labirinto, caminho):
    """
    Mostra o labirinto com o caminho marcado por '*'.
    """
    lab_copy = [linha[:] for linha in labirinto]
    for x, y in caminho[1:-1]:  # Ignora S e E
        lab_copy[x][y] = '*'
    for linha in lab_copy:
        print(' '.join(linha))

# -------------------------- Função Principal --------------------------

def main():
    try:
        linhas = int(input("Digite o número de linhas do labirinto: "))
        colunas = int(input("Digite o número de colunas do labirinto: "))
        probabilidade = float(input("Digite a probabilidade de haver um obstáculo (entre 0 e 1): "))

        labirinto = gerar_labirinto(linhas, colunas, probabilidade)

        print("\nLabirinto gerado:")
        for linha in labirinto:
            print(' '.join(linha))

        inicio, fim = encontrar_pontos(labirinto)
        caminho = a_star(labirinto, inicio, fim, permitir_diagonais=True)

        if caminho:
            print("\nCaminho encontrado (coordenadas):")
            print(caminho)
            print("\nLabirinto com caminho:")
            imprimir_labirinto_com_caminho(labirinto, caminho)
        else:
            print("\nSem solução possível para este labirinto.")
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# -------------------------- Execução --------------------------

if __name__ == "__main__":
    main()
    
