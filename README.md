# Funções de Ativação e suas Derivadas

## Introdução

As funções de ativação em redes neurais são funções matemáticas aplicadas à saída de um neurônio[^1^]. Elas são responsáveis por transformar a entrada linear em uma saída que é mais adequada para o contexto do problema, geralmente não-linear. Elas ajudam a rede a aprender de dados complexos, tomar decisões e prever resultados precisos. 

Neste documento, estamos explorando quatro funções de ativação diferentes: Sigmoide, Softsign, ReLU e Tanh. 

## Sigmoide

A função sigmoide é uma função de ativação que transforma qualquer número em um valor entre 0 e 1. Ela é útil para modelos onde precisamos prever a probabilidade como uma saída. A função sigmoide é expressa matematicamente como:

$$f(x) = \frac{1}{1 + e^{-x}}$$

A derivada da função sigmoide nos ajuda a entender como as mudanças na entrada afetam a saída:

$$f'(x) = f(x) \cdot (1 - f(x))$$

## Softsign

A função Softsign é uma alternativa à função de ativação tanh. Ela converge polinomialmente e produz uma saída entre -1 e 1. A função softsign é expressa matematicamente como:

$$f(x) = \frac{x}{1 + |x|}$$

A derivada da função Softsign nos mostra como pequenas mudanças na entrada afetam a saída:

$$f'(x) = \frac{1}{(1 + |x|)^2}$$

## ReLU

ReLU, ou Unidade Linear Retificada, é uma função de ativação que produz zero para qualquer valor negativo e x para qualquer valor positivo. A função ReLU é expressa matematicamente como:

$$f(x) = max(0, x)$$

O gráfico da derivada da ReLU é uma função degrau:

$$f'(x) = 1 \quad if \quad x > 0; \quad 0 \quad otherwise$$

## Tanh

A função Tanh, ou tangente hiperbólica, é semelhante à sigmoide, mas seu valor de saída varia de -1 a 1. A função tanh é expressa matematicamente como:

$$f(x) = tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}}$$

A derivada da função tanh mostra como pequenas mudanças na entrada mudam a saída:

$$f'(x) = 1 - (f(x))^2$$

## Código

O código Python usado para gerar os gráficos dessas funções e suas derivadas utiliza a biblioteca matplotlib para a visualização e a biblioteca numpy para cálculos numéricos.

Primeiro, definimos as funções de ativação e suas derivadas. Em seguida, geramos um conjunto de valores x usando a função `linspace` do numpy.

Para cada função de ativação, calculamos os valores y correspondentes e os plotamos em um subplot separado, junto com a sua derivada.

Os gráficos resultantes nos dão uma visualização clara de como cada função de ativação e sua derivada se comportam.

## Referências

[Acervo Lima - Funções de Ativação em Redes Neurais](https://acervolima.com/funcoes-de-ativacao-em-redes-neurais/)

[Wikipedia - Função de Ativação](https://pt.wikipedia.org/wiki/Fun%C3%A7%C3%A3o_de_ativa%C3%A7%C3%A3o)

[Medium - Understanding Activation Functions in Neural Networks](https://medium.com/the-theory-of-everything/understanding-activation-functions-in-neural-networks-9491262884e0)

[Stanford University - CS231n: Convolutional Neural Networks for Visual Recognition](http://cs231n.github.io/neural-networks-1/)
