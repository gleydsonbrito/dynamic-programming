# fibonacci Recursivo 20.1
def recursiveFib(n):
    if n <= 2:
        return 1
    return recursiveFib(n-1) + recursiveFib(n-2)


# print(recursiveFib(15))

F = []


def topDownFib(n):

    F.append(1)
    F.append(1)
    for i in range(2, len(F)):
        F[i] = -1

    return recursiveTopDownFib(n)


def recursiveTopDownFib(n):
    if F[n] == -1:
        F[n] = recursiveTopDownFib(n-1) + recursiveTopDownFib(n-2)
    return F[n]


print(topDownFib(15))
