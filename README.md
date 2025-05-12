# Projeto PathFinder

## 📌 Descrição

**PathFinder** é um projeto Python que implementa o algoritmo **A\*** (A-Star) para encontrar o menor caminho entre dois pontos em um labirinto 2D, evitando obstáculos e otimizando o custo total do trajeto. O algoritmo é utilizado em áreas como inteligência artificial, jogos e robótica para navegação eficiente.

---

## 🔍 Sobre o Algoritmo A\*

O A* é um algoritmo de busca informada que calcula o melhor caminho com base na fórmula:

```
F(n) = G(n) + H(n)
```

- **G(n)**: Custo real do início até o nó atual  
- **H(n)**: Estimativa (heurística) do custo até o destino

### Heurística Utilizada

- **Distância de Manhattan**:  
  ```
  h(n) = |x1 - x2| + |y1 - y2|
  ```

Opcionalmente, é possível ativar **movimentos diagonais**, com custo de √2.

---

## ⚙️ Como Executar

### 1. Clonar o Repositório

```bash
git clone https://github.com/seuusuario/pathfinder.git
cd pathfinder
```

### 2. Criar Ambiente Virtual (opcional, mas recomendado)

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### 3. Executar o Script

```bash
python main.py
```

O script utiliza um labirinto pré-definido no código, aplica o algoritmo A* e imprime o caminho encontrado no terminal.

---

## 🧠 Funcionalidades

- ✅ Algoritmo A* funcional  
- ✅ Heurística de Manhattan  
- ✅ Suporte a movimentos diagonais (opcional)  
- ✅ Marcação visual do caminho encontrado  
- ✅ Validação de entrada (exatamente 1 'S' e 1 'E')  
- ✅ Tratamento de erros  
- ✅ Código modularizado e comentado  

---

## 🧪 Exemplo de Execução

### Entrada:

```python
labirinto = [
    ['S', '0', '1', '0', '0'],
    ['0', '0', '1', '0', '1'],
    ['1', '0', '1', '0', '0'],
    ['1', '0', '0', 'E', '1']
]
```

### Saída:

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

## 📂 Estrutura

- `main.py`: Arquivo principal com toda a lógica
- `README.md`: Documentação do projeto
- (opcional) `labirintos/`: Pasta para entrada por arquivos

---

## 🧠 Complexidade

### Complexidade Assintótica

- **Melhor caso:** O(n), onde n = número de células livres
- **Pior caso:** O(n log n), devido à fila de prioridade (heap)

### Complexidade Ciclomática

- **Cálculo:** `M = E - N + 2P = 10 - 8 + 2(1) = 4`  
  A função `a_star()` apresenta **4 caminhos independentes**, indicando lógica bem estruturada e controle de fluxo claro.

---

## ✨ Possíveis Expansões

- Movimentos diagonais com ativação dinâmica ✅
- Terrenos com pesos variados ⏳
- Geração automática de labirintos ⏳
- Interface gráfica com PyGame ou Tkinter ⏳
- Entrada de labirinto via arquivo `.txt` ⏳
- Exportação do caminho em JSON ⏳

---

## 📌 Conclusão

O projeto **PathFinder** cumpre seu propósito de forma clara, eficiente e com foco em qualidade de código. É ideal para aprendizado e também serve como base para sistemas mais complexos de navegação e IA.

---

## 👨‍💻 Autor

Gabriel Afonso Infante Vieira — Estudante de Engenharia de Software
