Markdown

# PathFinder - Resolvendo o Labirinto 2D com o Algoritmo A*

## Descrição do Projeto

O projeto **PathFinder** implementa o renomado algoritmo de busca de caminho A* para encontrar o menor trajeto entre um ponto inicial ('S') e um ponto final ('E') dentro de um labirinto bidimensional. Desenvolvido para simular a tarefa de um robô de resgate, o programa navega pelo labirinto, evitando obstáculos e considerando diferentes custos de movimentação para determinar a rota mais eficiente.

Este projeto atende aos requisitos propostos, incluindo a implementação da heurística de Distância de Manhattan, tratamento de obstáculos, validação dos pontos de início/fim e a exibição do caminho encontrado. Além disso, foram adicionadas funcionalidades opcionais para tornar a solução mais robusta.

## Sobre o Algoritmo A* e o Labirinto

O Algoritmo A* é um algoritmo de busca de caminho eficiente e amplamente utilizado que combina características do algoritmo de Dijkstra (que encontra o menor caminho considerando custos) com uma heurística (uma estimativa da distância restante até o objetivo).

A* funciona avaliando cada célula potencial no labirinto com uma função de custo total $f(n)$:

$f(n) = g(n) + h(n)$

Onde:
- $g(n)$: É o custo acumulado para chegar à célula atual $n$ a partir do ponto de início.
- $h(n)$: É o custo estimado (heurística) para ir da célula atual $n$ até o ponto final.

Para este projeto, a heurística utilizada é a **Distância de Manhattan**, calculada como a soma das diferenças absolutas das coordenadas x e y entre dois pontos $(x_1, y_1)$ e $(x_2, y_2)$:

$h((x_1, y_1), (x_2, y_2)) = |x_1 - x_2| + |y_1 - y_2|$

O labirinto é representado por uma matriz 2D onde cada célula possui um valor que define seu tipo e custo associado.

## Regras do Labirinto Implementadas

O labirinto é uma grade 2D com as seguintes representações:

- `'0'`: Célula livre, custo de movimento base 1.
- `'1'`: Obstáculo, custo de movimento infinito (não é possível atravessar).
- `'2'`: Célula de "terreno difícil", custo de movimento base 5.
- `'S'`: Ponto de Início (Start), custo de movimento base 1.
- `'E'`: Ponto Final (End), custo de movimento base 1.

O robô pode se mover para células adjacentes (cima, baixo, esquerda, direita) e, como funcionalidade extra, também para as diagonais.

## Funcionalidades Extras Implementadas

Este projeto vai além dos requisitos básicos e inclui as seguintes funcionalidades opcionais:

1.  **Movimentos Diagonais:** O robô pode se mover nas 8 direções (cardeais e diagonais). O custo de um movimento diagonal é calculado como $\sqrt{2}$ vezes o custo base da célula de destino.
2.  **Custos Variáveis de Terreno:** Diferentes tipos de terreno ('0' e '2') têm custos distintos, permitindo que o A* encontre o caminho mais barato, não apenas o caminho com o menor número de passos. Obstáculos ('1') têm custo infinito.
3.  **Geração Automática de Labirintos:** O usuário pode definir as dimensões do labirinto e a probabilidade de ocorrência de obstáculos, gerando um labirinto aleatório para testar o algoritmo.
4.  **Validação de Pontos S/E:** O código verifica se há exatamente um ponto de início ('S') e um ponto de fim ('E') no labirinto gerado, levantando um erro caso contrário.
5.  **Tratamento de Labirintos Sem Solução:** Se o algoritmo A* explorar todas as possibilidades e não encontrar um caminho até o ponto 'E', ele reporta que não há solução possível.

## Como Executar o Projeto

### Pré-requisitos

- Python 3.6 ou superior

### Executar o Script

1.  Salve o código Python em um arquivo (ex: `maze_solver.py`).
2.  Abra um terminal ou prompt de comando.
3.  Navegue até o diretório onde salvou o arquivo.
4.  Execute o script Python:

    ```bash
    python maze_solver.py
    ```

5.  O programa solicitará que você insira as seguintes informações:
    - Número de linhas do labirinto.
    - Número de colunas do labirinto.
    - Probabilidade de haver um obstáculo (um valor entre 0 e 1).

### Entrada do Usuário

O programa espera 3 entradas via terminal:
- `linhas` (int): Número inteiro positivo para as linhas.
- `colunas` (int): Número inteiro positivo para as colunas.
- `probabilidade_obstaculo` (float): Um valor entre 0.0 e 1.0.

### Saída do Programa

A saída incluirá:
- O labirinto gerado.
- O caminho encontrado em formato de lista de coordenadas (se houver solução).
- O labirinto exibido novamente, com o caminho marcado por asteriscos ('*').
- Uma mensagem indicando que não há solução, se for o caso.

## Estrutura do Código

O código está organizado nas seguintes seções principais:

-   **Importações:** Importa as bibliotecas necessárias (`heapq` para a fila de prioridade, `math` para `inf` e `sqrt(2)`, `random` para a geração do labirinto).
-   **Funções Utilitárias:**
    -   `encontrar_pontos(labirinto)`: Localiza 'S' e 'E' e valida sua unicidade.
    -   `heuristica(a, b)`: Calcula a distância de Manhattan entre dois pontos.
    -   `custo_celula(valor)`: Retorna o custo de atravessar uma célula baseando-se em seu valor ('0', '1', '2', 'S', 'E').
    -   `gerar_labirinto(linhas, colunas, probabilidade_obstaculo)`: Cria uma matriz de labirinto aleatória com '0', '1', 'S' e 'E'.
-   **Algoritmo A\*:**
    -   `a_star(labirinto, inicio, fim, permitir_diagonais)`: Implementa o algoritmo A* usando uma fila de prioridade (`heapq`) para explorar o labirinto e encontrar o caminho otimizado. Considera movimentos cardeais, diagonais (opcionalmente, ativado na `main`), e custos variáveis de terreno.
-   **Impressão:**
    -   `imprimir_labirinto_com_caminho(labirinto, caminho)`: Gera uma representação visual do labirinto com o caminho encontrado marcado.
-   **Função Principal:**
    -   `main()`: Orquestra a execução do programa, lidando com entrada/saída do usuário, geração do labirinto, chamada ao A* e impressão dos resultados. Inclui tratamento básico de erros.

## Exemplo de Entrada e Saída

Considerando uma entrada do usuário para gerar um labirinto 5x5 com 20% de chance de obstáculos.

**Entrada (Exemplo de Labirinto Gerado):**

S 0 1 0 0
0 0 1 0 1
1 0 1 0 0
1 0 0 E 1
0 0 1 0 0


*(Note: O labirinto gerado será aleatório, então este é apenas um exemplo possível)*

**Saída (Exemplo de Caminho Encontrado e Labirinto com Caminho):**

Labirinto gerado:
S 0 1 0 0
0 0 1 0 1
1 0 1 0 0
1 0 0 E 1
0 0 1 0 0

Caminho encontrado (coordenadas):
[(0, 0), (1, 1), (2, 1), (3, 2), (3, 3)]

Labirinto com caminho:
S 0 1 0 0
0 * 1 0 1
1 * 1 0 0
1 0 * E 1
0 0 1 0 0



## Conclusão

Este projeto demonstra a aplicação prática do algoritmo A* para resolver o problema clássico de busca de caminho em labirintos 2D. A implementação considera custos variáveis de terreno e a possibilidade de movimentos diagonais, tornando a solução mais flexível e alinhada com cenários do mundo real onde o "custo" de deslocamento pode variar. A geração automática de labirintos facilita os testes em diferentes configurações.
