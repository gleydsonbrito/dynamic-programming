# fibonacci Recursivo 20.1
def recursiveFib(n):
    if n <= 2:
        return 1
    return recursiveFib(n-1) + recursiveFib(n-2)


# print(recursiveFib(15))
# Fibonacci Recursivo Top Down Alg. 20.2 e 20.3
F = [0] * 15


def topDownFib(m):
    n = len(F)
    F[0] = 1
    F[1] = 1
    for i in range(2, n):
        F[i] = -1

    return recursiveTopDownFib(m-1)


def recursiveTopDownFib(n):
    if F[n] == -1:
        F[n] = recursiveTopDownFib(n-1) + recursiveTopDownFib(n-2)
    return F[n]


# print(topDownFib(15))
