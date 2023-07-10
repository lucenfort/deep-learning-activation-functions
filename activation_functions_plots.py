import numpy as np
import matplotlib.pyplot as plt

# Definir as funções de ativação e suas derivadas
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def dsigmoid(x):
    return sigmoid(x) * (1 - sigmoid(x))

def softsign(x):
    return x / (1 + np.abs(x))

def dsoftsign(x):
    return 1 / ((1 + np.abs(x)) ** 2)

def relu(x):
    return np.maximum(0, x)

def drelu(x):
    return np.where(x > 0, 1.0, 0.0)

def tanh(x):
    return np.tanh(x)

def dtanh(x):
    return 1 - (tanh(x) ** 2)

# Gerar valores x
x = np.linspace(-10, 10, 1000)

# Preparar o layout do gráfico
fig, axs = plt.subplots(2, 2, figsize=(10, 6))

# Plotar as funções de ativação e suas derivadas em subplots separados
axs[0, 0].plot(x, sigmoid(x), label="Sigmoid", linewidth=2)
axs[0, 0].plot(x, dsigmoid(x), label="dSigmoid", linewidth=2)
axs[0, 0].legend(loc="upper left")

axs[0, 1].plot(x, softsign(x), label="Softsign", linewidth=2)
axs[0, 1].plot(x, dsoftsign(x), label="dSoftsign", linewidth=2)
axs[0, 1].legend(loc="upper left")

axs[1, 0].plot(x, relu(x), label="ReLU", linewidth=2)
axs[1, 0].plot(x, drelu(x), label="dReLU", linewidth=2)
axs[1, 0].legend(loc="upper left")

axs[1, 1].plot(x, tanh(x), label="Tanh", linewidth=2)
axs[1, 1].plot(x, dtanh(x), label="dTanh", linewidth=2)
axs[1, 1].legend(loc="upper left")

# Adicionar grid e título a cada subplot
for ax in axs.flat:
    ax.grid(True)
    ax.set(xlabel='x', ylabel='y')

# Mostrar o gráfico
plt.tight_layout()
plt.show()
