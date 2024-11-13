import numpy as np
from generators_v1 import LCG, GLCG, SLFG, RC4_32

# LCG generation:


N = 1000
list_LCG = []
x_0 = 5
for i in range(0, N):
    x_n = LCG(x_0)
    list_LCG.append(x_n)
    x_0 = x_n


N = 1000
list_GLCG = []
list_seed = [5, 10, 15]
for i in range(0, N):
    x_n = GLCG(list_seed)
    list_GLCG.append(x_n)
    del list_seed[0]
    list_seed.append(x_n)

print(list_GLCG)


N = 1000
list_SLFG = []
list_seed = [1, 2, 3, 4, 5]
for i in range(0, N):
    x_n = SLFG(list_seed)
    list_SLFG.append(x_n)
    del list_seed[0]
    list_seed.append(x_n)

print(list_SLFG)

print(RC4_32())
