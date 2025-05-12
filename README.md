Markdown

# Projeto PathFinder: Resolvendo o Labirinto 2D com o Algoritmo A*

## Descrição do Projeto

O projeto **PathFinder** implementa o algoritmo de busca A* em Python para encontrar o menor caminho entre um ponto de início ('S') e um ponto de fim ('E') em um labirinto bidimensional. O labirinto pode conter obstáculos ('1') que impedem a passagem. O algoritmo A* combina o custo do caminho já percorrido com uma função heurística para estimar o custo restante até o objetivo, buscando a solução de forma eficiente.

## Sobre o Problema: Encontrando o Caminho em um Labirinto 2D

Encontrar um caminho eficiente em um labirinto é um problema clássico em ciência da computação e inteligência artificial. Em um cenário como o de um robô de resgate, encontrar o menor caminho para um objetivo, evitando obstáculos, é crucial para otimizar o tempo e os recursos. O algoritmo A* se destaca por sua capacidade de encontrar a solução ótima (o caminho de menor custo) ao considerar tanto o custo já incorrido quanto uma estimativa inteligente do custo restante.

## Como Executar o Projeto

### 1. Pré-requisitos

Certifique-se de ter o Python instalado em seu sistema. Este projeto utiliza as seguintes bibliotecas padrão do Python:

- `heapq`: Para implementar a fila de prioridade necessária no algoritmo A*.
- `math`: Para funções matemáticas como `math.inf` e `math.sqrt` (utilizada para movimentos diagonais opcionais).
- `random`: Para a geração aleatória de labirintos.

Não são necessárias instalações adicionais de bibliotecas.

### 2. Executar o Script

Para executar o algoritmo, salve o código fornecido em um arquivo Python (por exemplo, `pathfinder.py`) e execute-o a partir do seu terminal:

```bash
python pathfinder.py
O programa solicitará as seguintes informações:

Número de linhas do labirinto.
Número de colunas do labirinto.
Probabilidade de haver um obstáculo (um valor entre 0 e 1 para a geração aleatória do labirinto).
Após fornecer essas informações, o programa gerará um labirinto aleatório, mostrará o labirinto, tentará encontrar o caminho usando o algoritmo A* (permitindo movimentos diagonais), e exibirá o caminho encontrado (em coordenadas) e o labirinto com o caminho destacado.

3. Exemplo de Entrada e Saída
Entrada (via terminal):

Digite o número de linhas do labirinto: 5
Digite o número de colunas do labirinto: 7
Digite a probabilidade de haver um obstáculo (entre 0 e 1): 0.2
Saída (exemplo - o labirinto e o caminho podem variar devido à geração aleatória):

Labirinto gerado:
S 0 0 1 0 0 0
0 1 0 0 1 0 0
0 0 0 1 0 1 0
1 0 1 0 0 0 E
0 0 0 1 0 0 0

Caminho encontrado (coordenadas):
[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (3, 3), (3, 4), (3, 5), (4, 5), (4, 6)]

Labirinto com caminho:
S * * 1 0 0 0
0 1 * 0 1 0 0
0 0 * 1 0 * 0
1 0 1 0 0 * E
0 0 0 1 0 * 0
Neste exemplo, '*' indica as células que fazem parte do menor caminho encontrado.

Explicação do Algoritmo A* Implementado
O algoritmo A* implementado neste projeto funciona da seguinte maneira:

Representação do Labirinto: O labirinto é representado como uma lista de listas (uma matriz 2D) onde cada elemento indica o tipo da célula ('0' para livre, '1' para obstáculo, 'S' para início, 'E' para fim).

Encontrar Pontos de Início e Fim (encontrar_pontos): Esta função itera pelo labirinto para encontrar as coordenadas exatas do ponto de início ('S') e do ponto de fim ('E'). Ela também valida se existe exatamente um de cada.

Função Heurística (heuristica): A função heurística utilizada é a distância de Manhattan entre dois pontos. Para dois pontos $(a_x, a_y)$ e $(b_x, b_y)$, a distância de Manhattan é calculada como:
$$h(a, b) = |a_x - b_x| + |a_y - b_y|$$
Esta heurística estima o número mínimo de movimentos (horizontais ou verticais) necessários para alcançar o objetivo a partir da célula atual.

Custo da Célula (custo_celula): Esta função define o custo para se mover para uma determinada célula. Na implementação atual:

Células livres ('0', 'S', 'E') têm um custo de 1.
Células com valor '2' (um exemplo de terreno mais difícil) têm um custo de 5.
Obstáculos ('1' ou qualquer outro valor não reconhecido) têm um custo infinito (math.inf), o que efetivamente impede o algoritmo de passar por eles.
Algoritmo A (a_star):*

Conjunto Aberto (Fila de Prioridade): Utiliza um heap de prioridade (heapq) para armazenar os nós a serem explorados. A prioridade de cada nó é dada por $f(n) = g(n) + h(n)$, onde:
$g(n)$ é o custo do caminho percorrido até o nó $n$.
$h(n)$ é a estimativa heurística do custo do nó $n$ até o objetivo.
Conjunto Fechado (Implícito): O conjunto de nós já avaliados é implicitamente mantido através do dicionário custo_ate.
Rastreamento do Caminho (veio_de): Um dicionário veio_de armazena o nó predecessor de cada nó no caminho mais curto encontrado até o momento. Isso permite reconstruir o caminho final.
Exploração de Vizinhos: Em cada iteração, o nó com a menor prioridade é removido do heap. Se este nó for o objetivo, o caminho é reconstruído. Caso contrário, seus vizinhos válidos (dentro dos limites do labirinto e não sendo obstáculos) são explorados.
Cálculo de Custos: Para cada vizinho, um novo custo é calculado ($novo_custo = custo_ate[atual] + custo_terreno$). Se este novo custo for menor do que o custo já conhecido para chegar ao vizinho, o custo é atualizado, o predecessor do vizinho é registrado, e o vizinho é adicionado ao heap com sua nova prioridade ($prioridade = novo_custo + heuristica(vizinho, fim)$).
Movimentos Diagonais (Opcional): A implementação permite movimentos diagonais se o parâmetro permitir_diagonais for True. O custo de um movimento diagonal é $\sqrt{2}$.
Sem Solução: Se o heap se esvaziar antes de o objetivo ser alcançado, significa que não há um caminho possível, e a função retorna None.
Impressão do Labirinto com Caminho (imprimir_labirinto_com_caminho): Esta função recebe o labirinto original e o caminho encontrado e cria uma cópia do labirinto onde as células pertencentes ao caminho (excluindo o início e o fim) são marcadas com '*'. Isso facilita a visualização do caminho no labirinto.

Função Principal (main): A função principal coordena todo o processo:

Solicita ao usuário as dimensões do labirinto e a probabilidade de obstáculos.
Gera o labirinto aleatoriamente.
Encontra os pontos de início e fim.
Chama o algoritmo A* para encontrar o caminho.
Imprime o labirinto gerado, o caminho encontrado (em coordenadas) e o labirinto com o caminho destacado.
Lida com possíveis erros, como a não existência de um ponto de início ou fim único.
Conclusão
Este projeto demonstra uma implementação eficaz do algoritmo de busca A* para resolver o problema de encontrar o menor caminho em um labirinto 2D. Ao combinar o custo real do caminho com uma heurística informada, o algoritmo A* explora o espaço de busca de forma inteligente, encontrando a solução ótima de maneira eficiente. A flexibilidade da função de custo da célula permite a extensão para cenários com diferentes tipos de terreno e custos de movimento.
