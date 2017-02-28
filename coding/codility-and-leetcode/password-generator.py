# generate password given sets
import numpy as np
from random import randint

def password(n, sets):
    passw = ''
    num_sets = len(sets)
    for i in range(n):
        if i < num_sets:
            set1 = sets[i]
            k = set1[randint(0, len(set1)-1)]
        else:
            rand_set = sets[randint(0, len(sets)-1)]
            k = rand_set[randint(0, len(rand_set)-1)]
        passw += str(k)
    return shuffle(passw)


def shuffle(passw):
    L = len(passw)
    for value, i in enumerate(passw):
        if i < (L-1):
            k = randint(i+1, L-1)
            current = passw[i]
            passw[i] = passw[k]
            passw[k] = current
    return passw
    
sets = [['a','b','c','d','e'], [0, 1, 2, 3, 5], ['A','B','C','D','E']]
print (password(8, sets))