def LCG(x_0):
    M = 2**10
    a = 3
    c = 7
    x_n = (a * x_0 + c) % M
    return x_n


def GLCG(list_seed):
    M = 2 ** 10
    list_a = [3, 7, 68]
    c = 5
    x_n = (list_seed[2]*list_a[0] + list_seed[1]*list_a[1]+ list_seed[2]*list_a[0] + c) % M
    return x_n


#Subtractive lagged Fibonacci generator:
# We have to know first 5 numbers x_0 ... x_4, because k = 5, l = 2

def SLFG(list_seed):
    M = 2 ** 10
    x_n = (list_seed[0] + list_seed[3]) % M
    return x_n


# K of length 5 (L=5)
def RC4_32():
    K = [3, 4, 9, 12, 20]
    L = len(K)
    m = 32
    S = [0] * m
    for i in range(0, m):
        S[i] = i
    j = 0
    for i in range(0, m):
        j = (j + S[i] + K[i % L]) % m
        temp = S[i]
        S[i] = S[j]
        S[j] = temp
    i = 0
    j = 0

    r = 0
    list = []
    while r < m:
        i = (i + 1) % m
        i = (j + S[i]) % m
        temp = S[i]
        S[i] = S[j]
        S[j] = temp
        x_r = S[(S[i] + S[j]) % m]
        list.append(x_r)
        r = r + 1

    return list

