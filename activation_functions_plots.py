import numpy as np
import plotly.graph_objects as go
import plotly.subplots as sp

# Definir funções de ativação e suas derivadas
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def dsigmoid(x):
    sig = sigmoid(x)
    return sig * (1 - sig)

def tanh(x):
    return np.tanh(x)

def dtanh(x):
    return 1 - (tanh(x) ** 2)

def softmax(x):
    exp_x = np.exp(x - np.max(x))  # Normalização para estabilidade numérica
    return exp_x / np.sum(exp_x)

def dsoftmax(x):
    s = softmax(x)
    return s * (1 - s)  # Derivada simplificada (equivalente à Sigmoid)

def relu(x):
    return np.maximum(0, x)

def drelu(x):
    return np.where(x > 0, 1.0, 0.0)

def leaky_relu(x, alpha=0.01):
    return np.where(x > 0, x, alpha * x)

def dleaky_relu(x, alpha=0.01):
    return np.where(x > 0, 1, alpha)

def elu(x, alpha=1.0):
    return np.where(x > 0, x, alpha * (np.exp(x) - 1))

def delu(x, alpha=1.0):
    return np.where(x > 0, 1, alpha * np.exp(x))

def softsign(x):
    return x / (1 + np.abs(x))

def dsoftsign(x):
    return 1 / ((1 + np.abs(x)) ** 2)

def swish(x):
    return x * sigmoid(x)

def dswish(x):
    sig = sigmoid(x)
    return sig + x * dsigmoid(x)

# Gerar valores de entrada
x = np.linspace(-10, 10, 1000)

# Lista das funções de ativação e suas derivadas, ordenadas da mais antiga para a mais recente
activations = [
    (sigmoid, dsigmoid, "Sigmoid"),
    (tanh, dtanh, "Tanh"),
    (softmax, dsoftmax, "Softmax"),  # Agora com derivada simplificada!
    (relu, drelu, "ReLU"),
    (leaky_relu, dleaky_relu, "Leaky ReLU"),
    (elu, delu, "ELU"),
    (softsign, dsoftsign, "Softsign"),
    (swish, dswish, "Swish"),
]

# Criar layout dinâmico com 4 colunas e número correto de linhas
n_cols = 4  # Número de colunas fixo
n_rows = -(-len(activations) // n_cols)  # Ajuste dinâmico de linhas (ceil divisão)

fig = sp.make_subplots(rows=n_rows, cols=n_cols, subplot_titles=[a[2] for a in activations])

# Cores padronizadas
activation_color = "#7D3C98"  # Violeta
derivative_color = "#E67E22"  # Laranja

# Adicionar cada função e sua derivada
for i, (act, dact, title) in enumerate(activations):
    row, col = divmod(i, n_cols)  # Calcula a posição correta
    row += 1  # Ajuste necessário para Plotly (começa em 1)
    col += 1  # Correção para evitar erro de indexação

    # Adiciona curva da função de ativação (violeta)
    fig.add_trace(go.Scatter(x=x, y=act(x), mode="lines", name=f"{title}",
                             line=dict(color=activation_color, width=2)), row=row, col=col)

    # Adiciona curva da derivada (laranja)
    if dact:
        fig.add_trace(go.Scatter(x=x, y=dact(x), mode="lines", name=f"d{title}",
                                 line=dict(color=derivative_color, dash="dash", width=2)), row=row, col=col)

# Ajustar layout dos gráficos interativos
fig.update_layout(
    title="Funções de Ativação e suas Derivadas",
    height=700, width=1400,
    showlegend=True,  # Ativar legenda para cada gráfico
    template="plotly_dark"  # Estilização moderna
)

# Exibir o gráfico interativo
fig.show()
