# 📌 PathFinder: Resolução de Labirintos 2D com A*

## 🔍 Descrição
O projeto PathFinder é uma implementação em Python do algoritmo A* (A-Star) para encontrar o menor caminho entre dois pontos em um labirinto 2D, evitando obstáculos e considerando diferentes custos de terreno. Desenvolvido para aplicações em robótica, desenvolvimento de jogos e sistemas de navegação inteligente. O projeto gera labirintos proceduralmente com controle sobre o tamanho e a densidade de obstáculos.

## 🧠 Sobre o Algoritmo A*

### Princípios Fundamentais
O A* combina de forma inteligente:
- **Custo real (G):** Distância percorrida desde o início
- **Heurística (H):** Estimativa até o destino usando distância de Manhattan
- **Fórmula otimizada:** $\(F(n) = G(n) + H(n)\)$

### Heurística Implementada
O projeto utiliza a distância de Manhattan como heurística para estimar o custo restante até o destino:

```python
def heuristica(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])  # Distância de Manhattan
Sistema de Movimento
O projeto suporta movimentos padrão (↑, ↓, ←, →) com custo 1 e movimentos diagonais (↖, ↗, ↙, ↘) com custo √2, se a opção de diagonais estiver habilitada.

⚙️ Configuração e Execução
Pré-requisitos
Python 3.x
Instalação e Uso
Executar o Script
O código está no arquivo pathfinder.py. Para executá-lo:

Bash

python pathfinder.py
O programa solicitará o número de linhas e colunas do labirinto, bem como a probabilidade de haver um obstáculo. Em seguida, o programa irá gerar o labirinto, encontrar o menor caminho utilizando o algoritmo A* e exibir o caminho encontrado, juntamente com uma representação visual do labirinto.

🧠 Funcionalidades Principais
Recurso	Descrição	Status
Algoritmo A* Completo	Implementação otimizada com heapq	✅
Geração de Labirintos	Customização de tamanho e densidade de obstáculos. O labirinto é gerado com células representando caminhos livres ('0'), obstáculos ('1'), início ('S') e fim ('E').	✅
Movimentos Diagonais	Ativação via parâmetro no algoritmo A*	✅
Sistema de Custos	Custos diferenciados para células: 1 para caminhos livres, início e fim; infinito para obstáculos; e 5 para um tipo de terreno mais difícil ('2').	✅
Validação Rigorosa	Verificação de existência e unicidade de pontos 'S' e 'E'.	✅
Visualização	Destaque do caminho encontrado no terminal, marcando as células do caminho com '*'.	✅

Exportar para as Planilhas
🧪 Exemplo de Uso
Entrada Interativa
O programa solicitará:

Número de linhas e colunas do labirinto.
Probabilidade de haver um obstáculo em cada célula (valor entre 0 e 1).
Exemplo de entrada:

Digite o número de linhas do labirinto: 5
Digite o número de colunas do labirinto: 5
Digite a probabilidade de haver um obstáculo (entre 0 e 1): 0.3
Saída
O programa exibe o labirinto gerado, o caminho encontrado (se existir) e o labirinto com o caminho destacado.

Exemplo de saída:

Labirinto gerado:
S 0 1 0 0
0 0 1 0 1
1 0 1 0 0
1 0 0 E 1
0 0 0 0 0

Caminho encontrado (coordenadas):
[(0, 0), (1, 0), (1, 1), (2, 1), (3, 1), (3, 2), (3, 3)]

Labirinto com caminho:
S 0 1 0 0
* * 1 0 1
1 * 1 0 0
1 * * E 1
0 0 0 0 0
📊 Análise de Complexidade
Desempenho
Cenário	Complexidade Temporal	Complexidade Espacial
Melhor Caso	O(b^d)	O(n)
Pior Caso	O(n log n)	O(n)

Exportar para as Planilhas
b: Fator de ramificação (número médio de vizinhos explorados).
d: Profundidade da solução.
n: Número total de nós no labirinto (linhas * colunas).
Métricas de Código
Complexidade Ciclomática: 4 (na função a_star)
Linhas de Código: ~100
Cobertura de Testes: Não implementada
🛠️ Estrutura do Projeto
O projeto é estruturado em um único arquivo, pathfinder.py, contendo as seguintes funções principais:

encontrar_pontos(labirinto): Encontra os pontos de início ('S') e fim ('E') no labirinto.
heuristica(a, b): Calcula a distância de Manhattan entre dois pontos.
custo_celula(valor): Define o custo de atravessar uma célula do labirinto.
gerar_labirinto(linhas, colunas, probabilidade_obstaculo): Gera um labirinto 2D aleatório.
a_star(labirinto, inicio, fim, permitir_diagonais): Implementa o algoritmo A*.
imprimir_labirinto_com_caminho(labirinto, caminho): Imprime o labirinto com o caminho destacado.
main(): Função principal que coordena a execução do programa.
✨ Roadmap e Futuras Melhorias
Interface Gráfica: Visualização interativa do labirinto e do caminho encontrado.
Sistema de Terrenos Avançado: Suporte para diferentes tipos de terreno com custos variados definidos pelo usuário.
Otimizações de Performance: Implementação com NumPy para grandes labirintos.
Funcionalidades Adicionais:
Exportação/importação de labirintos (JSON/CSV).
Modo benchmark para comparação de algoritmos.
Geração de labirintos com padrões específicos.
📌 Conclusão
Esta implementação do algoritmo A* fornece uma solução eficaz para encontrar o menor caminho em um labirinto 2D. O código é modular, bem comentado e segue as práticas recomendadas de programação em Python. Embora a funcionalidade básica esteja completa, o projeto pode ser expandido para incluir recursos adicionais, como uma interface gráfica e suporte para terrenos mais complexos.
