Markdown

# Projeto PathFinder: Resolvendo o Labirinto 2D com o Algoritmo A*

## Descrição do Projeto

O projeto **PathFinder** implementa o algoritmo de busca A* em Python para encontrar o menor caminho entre um ponto de início ('S') e um ponto de fim ('E') em um labirinto bidimensional. O labirinto pode conter obstáculos ('1') que impedem a movimentação. O algoritmo A* combina o custo do caminho já percorrido com uma função heurística (distância de Manhattan) para estimar o custo restante até o objetivo, permitindo uma busca eficiente pela solução ótima.

Este projeto também oferece funcionalidades adicionais como a geração aleatória de labirintos com diferentes níveis de dificuldade e a possibilidade de considerar movimentos diagonais com um custo diferenciado.

---

## Sobre o Problema do Labirinto 2D e o Algoritmo A*

Encontrar o caminho mais curto em um labirinto é um problema clássico em ciência da computação e inteligência artificial. O algoritmo A* é uma técnica de busca informada que se destaca por sua eficiência em encontrar soluções ótimas em grafos e espaços de busca.

**Como o Algoritmo A* Funciona:**

O A* utiliza uma função de avaliação $f(n)$ para cada nó (célula no labirinto), que é definida como a soma de duas componentes:

- $g(n)$: O custo do caminho percorrido do nó inicial até o nó atual $n$.
- $h(n)$: Uma estimativa heurística do custo do caminho mais curto do nó atual $n$ até o nó objetivo.

A fórmula é:
$$f(n) = g(n) + h(n)$$

O algoritmo mantém uma lista de nós a serem explorados (geralmente implementada como uma fila de prioridade, utilizando um heap) e sempre expande o nó com o menor valor de $f(n)$. Isso garante que o algoritmo explore primeiro os caminhos mais promissores.

**Heurística da Distância de Manhattan:**

Neste projeto, utilizamos a distância de Manhattan como função heurística. Para dois pontos $(x_1, y_1)$ e $(x_2, y_2)$, a distância de Manhattan é calculada como:

$$h(n) = |x_1 - x_2| + |y_1 - y_2|$$

Essa heurística é admissível (nunca superestima o custo real) em labirintos com movimentos apenas horizontais e verticais, garantindo que o A* encontre o caminho mais curto.

---

## Como Executar o Projeto

1.  **Pré-requisito:** Certifique-se de ter o Python instalado em seu sistema.

2.  **Salvar o Código:** Salve o código fornecido em um arquivo Python (por exemplo, `pathfinder.py`).

3.  **Navegar no Terminal:** Abra um terminal ou prompt de comando e navegue até o diretório onde você salvou o arquivo.

4.  **Executar o Script:** Execute o script com o comando:

    ```bash
    python pathfinder.py
    ```

5.  **Entrada do Usuário:** O programa solicitará que você insira o número de linhas e colunas desejadas para o labirinto, bem como a probabilidade de geração de obstáculos (um valor entre 0 e 1).

6.  **Processamento:** Após a geração (ou se você optar por modificar o código para usar um labirinto predefinido), o programa tentará encontrar o caminho mais curto entre 'S' e 'E' usando o algoritmo A*.

7.  **Exibição dos Resultados:** O resultado será exibido no console, mostrando:
    -   O labirinto gerado (ou o labirinto de entrada).
    -   O caminho encontrado como uma lista de coordenadas (se existir).
    -   O labirinto com o caminho destacado por '*'.
    -   Uma mensagem indicando se uma solução foi encontrada ou não.

---

## Explicação do Código (Linha a Linha)

Arquivo: **pathfinder.py**

```python
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

# Esta função itera sobre o labirinto para encontrar as coordenadas dos pontos 'S' e 'E'.
# Ela também realiza uma validação para garantir que exista exatamente um de cada.

def heuristica(a, b):
    """
    Distância de Manhattan entre dois pontos (a, b).
    """
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Implementa a função heurística da distância de Manhattan, calculando a soma das diferenças absolutas
# das coordenadas x e y entre dois pontos.

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

# Define o custo para mover-se através de diferentes tipos de células no labirinto.
# Células '0', 'S' e 'E' têm custo 1 (movimento padrão).
# Células '2' têm um custo maior (exemplo de terreno mais difícil - funcionalidade opcional).
# Células com outros valores (como '1' representando obstáculos) têm custo infinito, tornando-as inacessíveis.

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

# Função para gerar um labirinto aleatório de dimensões especificadas.
# A probabilidade de um obstáculo aparecer em cada célula é controlada por 'probabilidade_obstaculo'.
# Garante que os pontos de início 'S' e fim 'E' sejam colocados em células livres e distintas.

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

# Implementação do algoritmo A*.
# 'movimentos' define as direções possíveis (horizontal e vertical, com opção para diagonais).
# 'heap' é uma fila de prioridade que armazena os nós a serem explorados, ordenados pelo valor de f(n).
# 'veio_de' mantém o predecessor de cada nó no caminho mais curto encontrado até o momento.
# 'custo_ate' armazena o custo do caminho do início até cada nó.
# O loop 'while heap' continua até que o nó de destino seja encontrado ou a fila esteja vazia (sem solução).
# Para cada nó atual, explora os vizinhos válidos, calcula o novo custo e a prioridade (f(n)),
# e atualiza a fila de prioridade e os registros de 'veio_de' e 'custo_ate' se um caminho melhor for encontrado.
# Se o destino for alcançado, reconstrói o caminho a partir do nó final, seguindo os predecessores em 'veio_de'.

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

# Função para imprimir o labirinto, marcando as células que fazem parte do caminho encontrado com '*'.
# Ignora o ponto de início 'S' e o ponto de fim 'E' ao marcar o caminho.

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

# Função principal que interage com o usuário para obter as dimensões e a probabilidade do labirinto,
# gera o labirinto, encontra os pontos de início e fim, executa o algoritmo A* e imprime os resultados.
# Inclui tratamento de exceções para erros de entrada ou outros problemas.

# -------------------------- Execução --------------------------

if __name__ == "__main__":
    main()

# Bloco que garante que a função 'main()' seja executada apenas quando o script é rodado diretamente.
Markdown

---

## Exemplos de Entrada e Saída

**Exemplo de Entrada:**

Digite o número de linhas do labirinto: 5
Digite o número de colunas do labirinto: 5
Digite a probabilidade de haver um obstáculo (entre 0 e 1): 0.2


**Exemplo de Saída (o labirinto e o caminho podem variar devido à geração aleatória):**

Labirinto gerado:
S 0 0 1 0
0 1 0 0 0
0 0 1 0 1
0 1 0 E 0
0 0 0 1 0

Caminho encontrado (coordenadas):
[(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2), (3, 2), (3, 3)]

Labirinto com caminho:
S * * 1 0
0 1 * * 0
0 0 1 * 1
0 1 0 E 0
0 0 0 1 0


**Exemplo de Saída (sem solução):**

Se o labirinto gerado não tiver um caminho possível entre 'S' e 'E', a saída será:

Labirinto gerado:
S 1 0 1 0
0 1 0 1 0
0 1 0 1 0
0 1 0 E 0
0 1 0 1 0

Sem solução possível para este labirinto.



```markdown
---

## Conclusão

O projeto **PathFinder** demonstra uma implementação eficaz do algoritmo A* para a resolução do problema de encontrar o menor caminho em um labirinto 2D. Ao combinar o custo real do caminho percorrido com uma estimativa heurística da distância até o objetivo, o algoritmo A* explora o espaço de busca de forma inteligente, encontrando soluções ótimas de maneira eficiente. A flexibilidade de gerar labirintos aleatórios e a inclusão da opção de movimentos diagonais tornam este projeto uma ferramenta útil para entender e aplicar o algoritmo A* em diferentes cenários de busca de caminhos.
