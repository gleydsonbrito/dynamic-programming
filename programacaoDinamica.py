# fibonacci Recursivo 20.1
def recursiveFib(n):
    if n <= 2:  # caso base
        return 1
    # sucessivas chamadas reursivas
    return recursiveFib(n-1) + recursiveFib(n-2)


# print(recursiveFib(15))
# Fibonacci Recursivo Top Down Alg. 20.2 e 20.3
F = [0] * 15


def topDownFib(m):
    n = len(F)  # define o tamanho da lista
    F[0] = 1  # inicializa a lista
    F[1] = 1
    # preenche a lista com -1
    # para sinalizar a posição dos elementos que ainda não foram calculados
    for i in range(2, n):
        F[i] = -1

    # faz uma chamada recursica a partir do último elemtno da lista
    return recursiveTopDownFib(m-1)

# define as chamadas recursivas


def recursiveTopDownFib(n):
    if F[n] == -1:
        # armazena em f[n] os valores da chamada recursiva
        F[n] = recursiveTopDownFib(n-1) + recursiveTopDownFib(n-2)
    return F[n]


# print(topDownFib(15))

# alg. 20.4 fibonacci recursivo bottom up
def bottomUpFib(n):
    F = [0]*n  # inicializa uma lista com tantos zeros quantos forem o número de elementos

    # define o caso base, caso o n seja 1 ou 2, retorna imediatamente seu falor e encerra a chamda
    if n <= 2:
        return 1

    F[0] = 1  # inicaliza as 2 primeiras posições
    F[1] = 1  # necessárias a calculo das demais

    # percorre a lista, e atribui a cada posição
    # a soma das suas posições anteriores
    for i in range(2, len(F)):
        F[i] = F[i-1] + F[i-2]

    # retorna o último elemento da lista
    return F[n-1]


# print(bottomUpFib(10))

# algo. 20.5 do dcorte na barra de ferro
def cutIronBar(n, p):
    if n == 0:  # define o caso base das chamadas recursivas
        return 0

    l = -1  # define o valor mínimo para o lucro

    for i in range(0, n):
        # recupera o maior valor dentre os valores retornados das chamadas recursivas
        value = p[i] + cutIronBar(n - i - 1, p)
        if value > l:
            l = value
    # retorn o máximo valor obtido
    return l


#print(cutIronBar(8, [1, 5, 8, 9, 10, 17, 17, 20]))
B = []  # vetores globais
S = []

# função de inicialização


def cutIronBarTopDown(p, n=None):
    n = len(p)  # tamanmho das listas

    B = [-1]*n  # inicialização do vetor de barras com -1
    S = [0]*n  # inicialização do conjunto de soluções S

    B[0] = 0
    # chamada recursiva
    return recursiveCutIronBarTopDown(n, p)

# função de calculo da barra de ferro


def recursiveCutIronBarTopDown(k, p):
    # se B[k] for -1 essa solução ainda não foi avaliada
    if B[k] == -1:
        # inicaliza o licro com valor mínimo
        l = -1
        # percorre a lista de do fim para início recursivamente
        # obntendo o maior valor para cada conjunto de soluação
        for i in range(1, k):
            value = p[i] + recursiveCutIronBarTopDown(k-i-1, p)
            if value > l:
                l = value
                S[k] = i

        # retorna a melhor solução
        B[k] = l

    return B[k]


print(cutIronBar(8, [1, 5, 8, 9, 10, 17, 17, 20]))
print(S)
