import math
from itertools import permutations

def geneorder(n):
    n_fact = math.factorial(n)
    print(n_fact)
    num_list = list(range(1,n+1))
    for tup in permutations(num_list, n):
        for i in range(n):
            print(f'{tup[i]}', end=' ')
        print('' , end= '\n')

a = geneorder(6)
