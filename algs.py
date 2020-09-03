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

    # percorree a lista, e atribui a cada posição
    # a soma das suas posições anteriores
    for i in range(2, len(F)):
        F[i] = F[i-1] + F[i-2]

    # retorna o último elemento
    return F[n-1]


# print(bottomUpFib(10))
