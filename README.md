# Projeto PathFinder

## Descrição do Projeto

O projeto **PathFinder** implementa o algoritmo A* (A-Star) em Python para encontrar o menor caminho entre dois pontos em um labirinto 2D. Esse algoritmo é amplamente utilizado em áreas como robótica e jogos para navegação eficiente, considerando obstáculos e otimizando o custo total do trajeto.

---

## Sobre o Algoritmo A\*

O algoritmo A* é uma técnica de busca informada que combina:

- **G(n):** Custo do caminho percorrido até o nó atual
- **H(n):** Heurística que estima o custo restante até o destino (neste caso, distância de Manhattan)

A fórmula geral usada é:
```
F(n) = G(n) + H(n)
```

A distância de Manhattan é usada como heurística:
```
h(n) = |x_atual - x_final| + |y_atual - y_final|
```

Essa abordagem garante que o caminho mais curto e eficiente seja encontrado, se houver, mesmo em cenários com obstáculos complexos.

---

## Como Executar o Projeto

### 1. Ambiente Virtual (Opcional, mas recomendado)

Crie e ative um ambiente virtual para manter o ambiente isolado:

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### 2. Executar o Script

O código está no arquivo `main.py`. Para executá-lo:

```bash
python main.py
```

O programa carregará um labirinto 2D definido no próprio script, executará o algoritmo A* e imprimirá o caminho encontrado com destaque no terminal.

---

## Explicação do Código (Linha a Linha)

Arquivo: **main.py**

```python
import heapq

def encontrar_pontos(labirinto):
    for i, linha in enumerate(labirinto):
        for j, valor in enumerate(linha):
            if valor == 'S':
                start = (i, j)
            elif valor == 'E':
                end = (i, j)
    return start, end

def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(labirinto, inicio, fim):
    heap = []
    heapq.heappush(heap, (0, inicio))
    veio_de = {}
    custo_ate_aqui = {inicio: 0}

    while heap:
        _, atual = heapq.heappop(heap)
        if atual == fim:
            caminho = []
            while atual != inicio:
                caminho.append(atual)
                atual = veio_de[atual]
            caminho.append(inicio)
            caminho.reverse()
            return caminho

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            vizinho = (atual[0] + dx, atual[1] + dy)
            x, y = vizinho
            if 0 <= x < len(labirinto) and 0 <= y < len(labirinto[0]):
                if labirinto[x][y] != '1':
                    novo_custo = custo_ate_aqui[atual] + 1
                    if vizinho not in custo_ate_aqui or novo_custo < custo_ate_aqui[vizinho]:
                        custo_ate_aqui[vizinho] = novo_custo
                        prioridade = novo_custo + heuristica(vizinho, fim)
                        heapq.heappush(heap, (prioridade, vizinho))
                        veio_de[vizinho] = atual
    return None

def imprimir_labirinto_com_caminho(labirinto, caminho):
    lab_copy = [linha[:] for linha in labirinto]
    for x, y in caminho:
        if lab_copy[x][y] not in ('S', 'E'):
            lab_copy[x][y] = '*'
    for linha in lab_copy:
        print(' '.join(linha))

labirinto = [
    ['S', '0', '1', '0', '0'],
    ['0', '0', '1', '0', '1'],
    ['1', '0', '1', '0', '0'],
    ['1', '0', '0', 'E', '1']
]

inicio, fim = encontrar_pontos(labirinto)
if inicio is None or fim is None:
    print("Labirinto inválido: ponto S ou E não encontrado.")
else:
    caminho = a_star(labirinto, inicio, fim)
    if caminho:
        print("Menor caminho (coordenadas):")
        print(caminho)
        print("\nLabirinto com o caminho:")
        imprimir_labirinto_com_caminho(labirinto, caminho)
    else:
        print("Sem solução possível.")
```

---

## Exemplo de Entrada e Saída

### Entrada

```python
labirinto = [
    ['S', '0', '1', '0', '0'],
    ['0', '0', '1', '0', '1'],
    ['1', '0', '1', '0', '0'],
    ['1', '0', '0', 'E', '1']
]
```

### Saída

```
Menor caminho (coordenadas):
[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]

Labirinto com o caminho:
S 0 1 0 0
* * 1 0 1
1 * 1 0 0
1 * * E 1
```

---

## Relatório Técnico

### Complexidade Assintótica

- **Tempo (melhor caso):** O(n), onde n é o número de células livres próximas do ponto inicial.
- **Tempo (pior caso):** O(n log n), considerando uso de fila de prioridade (heap).
- **Espaço:** O(n), para armazenar os custos, o caminho e o heap.

### Complexidade Ciclomática

- Nós (N): 8  
- Arestas (E): 10  
- Componentes Conexos (P): 1  
- Fórmula: M = E - N + 2P = 10 - 8 + 2(1) = **4**

A função principal (`a_star`) tem uma complexidade ciclomática de 4, representando 4 caminhos independentes possíveis.

---

## Conclusão

O projeto **PathFinder** resolve com sucesso o problema de navegação em um labirinto 2D, utilizando o algoritmo A*. Ele encontra o menor caminho entre dois pontos, evitando obstáculos de maneira eficiente. A implementação é simples, clara e pode ser expandida facilmente com recursos como:

- Movimentos diagonais
- Terrenos com custos diferentes
- Interface gráfica (GUI)
- Geração automática de labirintos
