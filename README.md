PathFinder - Resolvendo o Labirinto 2D com o Algoritmo A*

Descrição do Projeto

O projeto PathFinder implementa o algoritmo A* (A-estrela) em Python para encontrar o caminho mais curto entre um ponto inicial ('S') e um ponto final ('E') em um labirinto 2D. Este algoritmo é fundamental em inteligência artificial e robótica para navegação e planejamento de rotas. O sistema permite a geração automática de labirintos, onde o robô simulado deve evitar obstáculos e considerar custos de movimento variáveis para alcançar seu objetivo da forma mais eficiente.

Sobre o Algoritmo A*

O algoritmo A* é um algoritmo de busca de caminho que encontra a rota de menor custo entre um nó inicial e um nó final em um grafo. Ele é amplamente reconhecido por sua eficiência e por garantir a otimalidade da solução (encontrar o caminho mais curto) se a heurística utilizada for admissível.

A* funciona avaliando os nós através da seguinte função:
f(n) = g(n) + h(n)

Onde:
g(n): É o custo real do caminho percorrido desde o nó inicial até o nó n. No contexto deste projeto, movimentos horizontais/verticais em células normais ('0', 'S', 'E') têm custo 1. Movimentos diagonais em células normais têm custo raiz_quadrada_de_2. Células de "terreno difícil" ('2') têm um custo base multiplicado (ex: 5 para movimento normal, 5 * raiz_quadrada_de_2 para diagonal).
h(n): É a função heurística, que estima o custo do caminho mais barato do nó n até o nó destino. Uma heurística comum e admissível para grades é a Distância de Manhattan:
h((x1, y1), (x2, y2)) = |x1 - x2| + |y1 - y2|
Esta heurística calcula a soma das diferenças absolutas das coordenadas, representando o caminho mais curto em uma grade se apenas movimentos horizontais e verticais fossem permitidos. Mesmo com diagonais, ela permanece admissível (não superestima o custo).

O algoritmo A* utiliza uma fila de prioridade (min-heap) para gerenciar os nós abertos (a serem visitados), sempre escolhendo expandir o nó com o menor valor f(n). Ele mantém um registro dos custos para alcançar cada nó e o caminho pelo qual foram alcançados, atualizando-os conforme encontra rotas melhores.

Como Executar o Projeto

Pré-requisitos
Python 3.x instalado.

Ambiente Virtual (Opcional, mas recomendado)
Para isolar as dependências do projeto, é uma boa prática utilizar um ambiente virtual:

Crie um ambiente virtual (ex: .venv)
python3 -m venv .venv

Ative o ambiente virtual
Linux/macOS:
source .venv/bin/activate
Windows (PowerShell):
.venv\Scripts\Activate.ps1
Windows (CMD):
.venv\Scripts\activate.bat

Executar o Script
Supondo que o código principal esteja salvo como seu_arquivo_principal.py (substitua pelo nome real do seu arquivo):

python seu_arquivo_principal.py

O programa solicitará interativamente:

O número de linhas do labirinto.
O número de colunas do labirinto.
A probabilidade de uma célula ser um obstáculo (valor entre 0 e 1).
Após a entrada, o labirinto gerado será exibido, seguido pelo caminho encontrado (se houver) e o labirinto com o caminho destacado.

Explicação do Código (Principais Funções e Estrutura do A*)

O código é modularizado em várias funções para lidar com a geração do labirinto, busca de pontos, cálculo de custos, heurística e a implementação do A*.

Funções Utilitárias Principais:

gerar_labirinto(linhas, colunas, probabilidade_obstaculo): Cria e retorna uma matriz 2D (labirinto) com obstáculos ('1'), caminhos livres ('0'), um ponto de início ('S') e um ponto de fim ('E'), posicionados aleatoriamente e de forma válida.
encontrar_pontos(labirinto): Localiza e retorna as coordenadas dos pontos 'S' e 'E'. Valida se existe exatamente um de cada.
heuristica(a, b): Calcula a distância de Manhattan entre os pontos a e b.
custo_celula(valor): Define o custo de movimento para uma célula baseado no seu conteúdo (ex: 1 para '0', 5 para '2', infinito para '1').

Algoritmo A* (a_star):

A função a_star(labirinto, inicio, fim, permitir_diagonais=True) é o núcleo da lógica de busca de caminho. Abaixo, um trecho da estrutura e lógica principal:

import heapq
import math

[...] outras funções utilitárias
def a_star(labirinto, inicio, fim, permitir_diagonais=False):
movimentos = [(-1,0), (1,0), (0,-1), (0,1)] # Movimentos cardeais
if permitir_diagonais:
movimentos += [(-1,-1), (-1,1), (1,-1), (1,1)] # Adiciona diagonais

heap = [] # Fila de prioridade (min-heap)
heapq.heappush(heap, (0, inicio)) # (prioridade_f, nó)

veio_de = {} # Dicionário para reconstruir o caminho: vizinho -> atual
custo_ate = {inicio: 0} # Dicionário g(n): nó -> custo_desde_o_inicio

while heap:
    _, atual = heapq.heappop(heap) # Nó com menor f(n)

    if atual == fim:
        # Caminho encontrado, reconstrói e retorna
        caminho = []
        # [...] Lógica de reconstrução
        return caminho[::-1]

    for dx, dy in movimentos:
        vizinho = (atual[0] + dx, atual[1] + dy)

        # Verifica limites do labirinto
        if not (0 <= vizinho[0] < len(labirinto) and 0 <= vizinho[1] < len(labirinto[0])):
            continue

        valor_vizinho = labirinto[vizinho[0]][vizinho[1]]
        custo_terreno_base = custo_celula(valor_vizinho)

        if custo_terreno_base == math.inf: # Obstáculo
            continue

        # Calcula custo do movimento (considerando diagonal)
        fator_diagonal = math.sqrt(2) if (abs(dx) + abs(dy) == 2 and permitir_diagonais) else 1
        custo_movimento = custo_terreno_base * fator_diagonal

        novo_custo_g = custo_ate[atual] + custo_movimento

        if vizinho not in custo_ate or novo_custo_g < custo_ate[vizinho]:
            custo_ate[vizinho] = novo_custo_g
            prioridade_f = novo_custo_g + heuristica(vizinho, fim)
            heapq.heappush(heap, (prioridade_f, vizinho))
            veio_de[vizinho] = atual

return None # Nenhum caminho encontrado
Função Principal (main):
Orquestra a execução: coleta entradas do usuário, chama gerar_labirinto, encontrar_pontos, a_star, e imprimir_labirinto_com_caminho para mostrar o resultado.

Relatório Técnico

Complexidade Assintótica do Algoritmo A*

Complexidade Temporal:
A complexidade temporal do A* depende da qualidade da heurística e da estrutura do grafo.
No pior caso (por exemplo, com uma heurística pouco informativa ou em grafos específicos), pode ser exponencial: O(b^d), onde b é o fator de ramificação (número médio de sucessores de um nó) e d é a profundidade da solução.
Com uma heurística consistente e admissível (como a Distância de Manhattan em uma grade) e usando uma fila de prioridade implementada com um heap binário, a complexidade é tipicamente O(E log V) ou, para grades, O(N log N), onde N é o número de células (vértices V) e E é o número de possíveis movimentos (arestas). Em alguns casos, pode aproximar-se de O(N) se a heurística for muito boa.

Complexidade Espacial:
A complexidade espacial é determinada principalmente pelo armazenamento dos nós na fila de prioridade (open_set) e dos nós já visitados ou com custos calculados (closed_set ou custo_ate e veio_de). No pior caso, pode ser necessário armazenar todos os nós: O(V) ou O(N) para uma grade.

Complexidade Ciclomática

A Complexidade Ciclomática é uma métrica de software que quantifica a complexidade de um programa medindo o número de caminhos linearmente independentes através do código-fonte. É calculada usando o grafo de fluxo de controle do programa.
Fórmula: M = E - N + 2P
(onde E = número de arestas, N = número de nós, P = número de componentes conectados no grafo). Alternativamente, para um único programa ou função sem goto, M = (Número de pontos de decisão) + 1.

Para a função a_star principal, que contém múltiplos laços (while heap, for dx, dy in movimentos, while atual in veio_de para reconstrução) e condicionais (if atual == fim, if limites_ok, if obstaculo, if novo_custo_melhor, etc.), a complexidade ciclomática será consideravelmente maior que a de uma função simples. Uma análise precisa envolveria desenhar o grafo de fluxo de controle detalhado para a função a_star.

Por exemplo, apenas a função a_star possui aproximadamente 9-11 pontos de decisão principais (dependendo de como se contam os predicados compostos), o que levaria a uma complexidade ciclomática para essa função na ordem de M aproximadamente 10 a 12.
Uma análise exaustiva da complexidade ciclomática para todo o script envolveria a soma das complexidades de suas funções ou uma análise do grafo de chamadas.

Nota: A visualização do Grafo de Fluxo para funções complexas como a_star requer ferramentas específicas ou um desenho manual detalhado e não é fornecida aqui.

Exemplo de Entrada e Saída

(Conforme fornecido anteriormente, mostrando a interação, o labirinto gerado, o caminho em coordenadas e o labirinto com o caminho destacado. Se nenhum caminho for encontrado, a saída será "Sem solução possível para este labirinto.")

Interação com o Usuário:

Digite o número de linhas do labirinto: 5
Digite o número de colunas do labirinto: 5
Digite a probabilidade de haver um obstáculo (entre 0 e 1): 0.2

Labirinto Gerado (Exemplo):

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

1 0 1 0
0 1 0 1 E 0 0 0 0 0 1
Conclusão

O projeto PathFinder implementa com sucesso o algoritmo A* para navegação em labirintos 2D. A solução considera diferentes custos de terreno e a possibilidade de movimentos diagonais, oferecendo uma ferramenta robusta para encontrar o caminho ótimo. A estrutura do código e a documentação visam facilitar o entendimento e a execução do projeto, cumprindo os objetivos de demonstrar a aplicação prática do A* em problemas de busca de caminho.
