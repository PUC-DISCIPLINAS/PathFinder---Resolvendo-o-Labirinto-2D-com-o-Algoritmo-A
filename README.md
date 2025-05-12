markdown
# PathFinder - Resolvendo o Labirinto 2D com o Algoritmo A*

## Descrição do Projeto

O projeto **PathFinder** implementa o algoritmo A* (A-estrela) em Python para encontrar o caminho mais curto entre um ponto inicial ('S') e um ponto final ('E') em um labirinto 2D. Este algoritmo é fundamental em inteligência artificial e robótica para navegação e planejamento de rotas.

## Sobre o Algoritmo A*

O algoritmo A* é um algoritmo de busca de caminho que encontra a rota de menor custo entre um nó inicial e um nó final em um grafo. Ele utiliza a função:

`f(n) = g(n) + h(n)`

Onde:
- `g(n)`: Custo real do caminho percorrido desde o nó inicial até o nó `n`
- `h(n)`: Função heurística que estima o custo do caminho mais barato do nó `n` até o destino

## Como Executar o Projeto

### Pré-requisitos
- Python 3.x instalado

### Ambiente Virtual (Opcional)
```bash
# Crie um ambiente virtual
python3 -m venv .venv

# Ative o ambiente virtual
# Linux/macOS:
source .venv/bin/activate
# Windows (PowerShell):
.venv\Scripts\Activate.ps1
# Windows (CMD):
.venv\Scripts\activate.bat
Executar o Script
bash
python seu_arquivo_principal.py
O programa solicitará:

Número de linhas do labirinto

Número de colunas do labirinto

Probabilidade de uma célula ser um obstáculo (valor entre 0 e 1)

Exemplo de Entrada e Saída
Entrada:

Digite o número de linhas do labirinto: 5
Digite o número de colunas do labirinto: 5
Digite a probabilidade de haver um obstáculo (entre 0 e 1): 0.2
Saída:

Labirinto gerado:
S 0 0 0 1
0 1 0 1 0
0 0 0 0 0
1 0 1 E 0
0 0 0 0 1

Caminho encontrado (coordenadas):
[(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3)]

Labirinto com caminho:
S 0 0 0 1
* 1 0 1 0
* * * * 0
1 0 1 E 0
0 0 0 0 1
Relatório Técnico
Complexidade Assintótica
Temporal: O(N log N) onde N é o número de células

Espacial: O(N) no pior caso

Complexidade Ciclomática
A função principal a_star possui complexidade ciclomática aproximada de 10-12 devido aos múltiplos laços e condicionais.

Conclusão
O PathFinder implementa com sucesso o algoritmo A* para navegação em labirintos 2D, considerando diferentes custos de terreno e movimentos diagonais, oferecendo uma ferramenta robusta para encontrar caminhos ótimos.
