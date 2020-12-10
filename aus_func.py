import math
from random import random

# diff
def diff(Lst):
    Lst1 = Lst[1:]+[0]
    r = []
    for x in zip(Lst,Lst1):
        r.append(x[0]-x[1])
    return r

## std

def std(L):
    N = len(L)
    m = sum(L)/N
    V_ = 0
    for x in L:
        V_ += (x - m)**2
    V = V_/N
    return math.sqrt(V)

## diff str
# each letter comparison with it corespondent.
# difference of ascii code (absolute)


def diff_lst_str(l_St):
    l_St1 = l_St[1:] + [l_St[0]]
    r = []
    for s in zip(l_St,l_St1):
        r.append(diff_str(s))
    return r


def diff_str(s):
    out = 0
    for x, y in zip(map(ord, s[0].decode('utf-8')), map(ord, s[1].decode('utf-8'))):
        out += abs(x-y)
    return out


def generate_password(L):
    r = ''
    for _ in range(L):
        x = int(random()*1000)
        if x:
            r += chr(x)
        else:
            r += ';'
    return bytes(r, 'utf-8')


def generate_passwords(K):
    r = []
    L = 12  # random
    for _ in range(K):
        r.append(generate_password(L))
    return r


def unique_values(X):
    return len(set(X))


def modlus_str(s, N):
    n = 0
    for x in s.decode('utf-8'):
        d = n + ord(x)
        n = (d % N)*10
    return int(n/10)
