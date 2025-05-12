Markdown

# PathFinder - Resolvendo o Labirinto 2D com o Algoritmo A*

## Descrição do Projeto

O projeto **PathFinder** implementa o algoritmo A* (A-estrela) em Python para encontrar o caminho mais curto entre um ponto inicial ('S') e um ponto final ('E') em um labirinto 2D. Este projeto foi desenvolvido para simular um robô de resgate que precisa navegar por um ambiente com obstáculos, calculando a rota mais eficiente. O labirinto pode ser gerado automaticamente com dimensões e densidade de obstáculos especificadas pelo usuário.

---

## Sobre o Algoritmo A*

O algoritmo A* é um algoritmo de busca de caminho amplamente utilizado que encontra o caminho de menor custo entre um nó inicial e um nó final em um grafo. Ele é conhecido por sua eficiência e otimalidade. O A* combina as vantagens do Algoritmo de Dijkstra (que prioriza caminhos já explorados) e da Busca Gulosa Best-First (que usa uma heurística para estimar o custo até o destino).

A principal característica do A* é o uso da função de avaliação $f(n)$, calculada para cada nó $n$:

$f(n) = g(n) + h(n)$

Onde:
-   $g(n)$: É o custo real do caminho desde o nó inicial até o nó $n$. No contexto deste projeto, cada movimento horizontal ou vertical tem custo 1, e movimentos diagonais têm custo $\sqrt{2}$. Células com terreno especial ('2') têm um custo base maior (5).
-   $h(n)$: É a função heurística que estima o custo do caminho mais barato do nó $n$ até o nó destino. Uma heurística admissível (que nunca superestima o custo real) é crucial para garantir que o A* encontre o caminho mais curto.

### Heurística de Manhattan

Neste projeto, a heurística utilizada é a **Distância de Manhattan**:
$h((x_1, y_1), (x_2, y_2)) = |x_1 - x_2| + |y_1 - y_2|$

Esta heurística calcula a soma das diferenças absolutas das coordenadas $x$ e $y$ entre o nó atual e o nó destino. Ela é apropriada para grades onde o movimento é restrito a direções horizontais e verticais, mas também funciona bem como uma estimativa quando movimentos diagonais são permitidos, pois continua sendo admissível.

O algoritmo A* mantém uma fila de prioridade (min-heap) dos nós a serem visitados, priorizando aqueles com o menor valor $f(n)$. Ele explora o nó com menor $f(n)$, atualiza os custos dos vizinhos e os adiciona à fila. O processo continua até que o nó destino seja alcançado ou a fila de prioridade esteja vazia (indicando que não há caminho).

---

## Funcionalidades Implementadas

-   **Geração Automática de Labirintos:** O usuário pode definir o número de linhas, colunas e a probabilidade de obstáculos para gerar labirintos aleatórios.
-   **Movimento em 8 Direções:** O algoritmo A* implementado permite movimentos nas quatro direções cardeais (cima, baixo, esquerda, direita) e, opcionalmente, nas quatro direções diagonais.
    -   Custo de movimento horizontal/vertical: 1 (para células normais).
    -   Custo de movimento diagonal: $\sqrt{2}$ (para células normais).
-   **Custos Variados por Célula:** O labirinto pode conter células com diferentes custos de travessia (ex: '2' representa terreno difícil com custo base 5).
-   **Validação:** O programa verifica se há exatamente um ponto de início ('S') e um ponto de fim ('E') no labirinto.
-   **Exibição Clara do Resultado:** O caminho encontrado é exibido como uma lista de coordenadas e também destacado visualmente no labirinto impresso.

---

## Como Executar o Projeto

### 1. Pré-requisitos

-   Python 3.x instalado.

### 2. Ambiente Virtual (Opcional, mas recomendado)

Para evitar conflitos de dependência com outros projetos Python, é uma boa prática criar e ativar um ambiente virtual:

```bash
# Crie um ambiente virtual (por exemplo, chamado .venv)
python3 -m venv .venv

# Ative o ambiente virtual
# Em Linux/macOS:
source .venv/bin/activate
# Em Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Em Windows (CMD):
.venv\Scripts\activate.bat
3. Executar o Script
Supondo que o código esteja em um arquivo chamado pathfinder_a_star.py (ou o nome que você deu ao arquivo principal contendo a função main):

Bash

python pathfinder_a_star.py
O programa solicitará que o usuário insira:

O número de linhas do labirinto.
O número de colunas do labirinto.
A probabilidade de haver um obstáculo em cada célula (um valor entre 0 e 1, por exemplo, 0.3 para 30% de chance).
Após a entrada, o labirinto gerado será exibido, seguido pelo caminho encontrado (se existir) e o labirinto com o caminho destacado.

Explicação do Código (Principais Funções)
gerar_labirinto(linhas, colunas, probabilidade_obstaculo):
Cria uma matriz 2D representando o labirinto. Preenche aleatoriamente as células com obstáculos ('1') com base na probabilidade fornecida e posiciona os pontos de início ('S') e fim ('E') em locais válidos e distintos.

encontrar_pontos(labirinto):
Varre o labirinto para localizar as coordenadas dos pontos 'S' (início) e 'E' (fim). Valida se existe exatamente um de cada, lançando um erro caso contrário.

heuristica(a, b):
Calcula a distância de Manhattan entre dois pontos a e b (tuplas de coordenadas).

custo_celula(valor):
Retorna o custo para atravessar uma célula com base no seu valor.

'0', 'S', 'E': custo 1 (caminho livre).
'2': custo 5 (terreno mais difícil).
'1' (ou outros): math.inf (obstáculo).
a_star(labirinto, inicio, fim, permitir_diagonais=False):
É o coração do projeto, implementando o algoritmo A*.

Inicializa uma fila de prioridade (heapq) com o nó inicial (custo 0).
Mantém dicionários para veio_de (para reconstruir o caminho) e custo_ate (o custo $g(n)$ para cada nó alcançado).
Em cada iteração, remove o nó com a menor prioridade ($f(n) = g(n) + h(n)$) da fila.
Se o nó atual for o destino, reconstrói e retorna o caminho.
Caso contrário, explora os vizinhos válidos (dentro dos limites, não obstáculos).
Para cada vizinho, calcula o novo custo ($g(n)$) para alcançá-lo.
Se um caminho mais curto para o vizinho for encontrado, atualiza seu custo_ate, veio_de, e o adiciona (ou atualiza sua prioridade) na fila de prioridade.
Se a fila ficar vazia e o destino não for alcançado, retorna None (sem solução).
Considera movimentos diagonais e custos de terreno diferenciados se permitir_diagonais for True e se a célula tiver um custo específico.
imprimir_labirinto_com_caminho(labirinto, caminho):
Cria uma cópia do labirinto e marca as células do caminho encontrado com '*' (exceto o início e o fim) para visualização.

main():
Função principal que gerencia a interação com o usuário, chama a geração do labirinto, a execução do A* e a exibição dos resultados. Inclui tratamento de erros para entradas inválidas ou situações onde o labirinto não tem solução.

Exemplo de Entrada e Saída
Interação com o Usuário:
Digite o número de linhas do labirinto: 5
Digite o número de colunas do labirinto: 5
Digite a probabilidade de haver um obstáculo (entre 0 e 1): 0.2
Labirinto Gerado (Exemplo):
(A saída exata variará devido à aleatoriedade)

Labirinto gerado:
S 0 0 0 1
0 1 0 1 0
0 0 0 0 0
1 0 1 E 0
0 0 0 0 1
Caminho Encontrado:
Caminho encontrado (coordenadas):
[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3)]
Labirinto com Caminho Destacado:
Labirinto com caminho:
S 0 0 0 1
* 1 0 1 0
* * * * 0
1 0 1 E 0
0 0 0 0 1
Exemplo sem Solução:
Se um labirinto for gerado onde 'E' é inacessível a partir de 'S':

Labirinto gerado:
S 1 E
0 1 0
0 0 0

Sem solução possível para este labirinto.
Requisitos de Implementação Atendidos
Entrada de matriz 2D: O labirinto é gerado automaticamente com base nas dimensões fornecidas pelo usuário.
Validação de S e E: A função encontrar_pontos garante que o labirinto contenha exatamente um ponto 'S' e um 'E' antes de executar o algoritmo.
Retorno "Sem solução": Se o algoritmo A* não encontrar um caminho entre 'S' e 'E', o programa informa "Sem solução possível para este labirinto."
Conclusão
O projeto PathFinder demonstra com sucesso a implementação do algoritmo A* para resolver o problema de busca de caminho em labirintos 2D. Ele incorpora funcionalidades como geração de labirintos, consideração de custos de movimento variáveis (incluindo diagonais e tipos de terreno), e uma clara apresentação dos resultados. O código é estruturado para ser compreensível e extensível, fornecendo uma base sólida para futuras melhorias ou aplicações em contextos mais complexos de navegação autônoma.
