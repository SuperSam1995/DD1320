import bcrypt
from aus_func import diff,diff_lst_str,std

salt = bcrypt.gensalt(6)

A = [bytes(str(x),'utf-8') for x in range(100)]
B = [bytes(chr(x),'utf-8') for x in range(ord('a'),ord('z'))]
C = [bytes(chr(x),'utf-8') for x in range(ord('A'),ord('Z'))]

D = []
for x in A:
    for y in B:
        D.append(y+x)


#### for the bcrypt
Numbers = [bcrypt.hashpw(x,salt) for x in A]
SmallL = [bcrypt.hashpw(x,salt) for x in B]
CapitalL = [bcrypt.hashpw(x,salt) for x in C]


## compare
G = diff_lst_str(Numbers)
V = std(G)
medel = 0
print("Standard deviation (higher is better) of Bcrypt (Numbers):")
print(V)
medel += V

G = diff_lst_str(SmallL)
V = std(G)
print("Standard deviation (higher is better) of Bcrypt (Small Letters):")
print(V)
medel += V

G = diff_lst_str(CapitalL)
V = std(G)
print("Standard deviation (higher is better) of Bcrypt (Capitals):")
print(V)
medel += V
print("Average standard deviation for Bcrypt is:")
print(medel/3)

Numbers = [hash(x) for x in A]
SmallL = [hash(x) for x in B]
CapitalL = [hash(x) for x in C]
medel2 = 0
#### for the hash
G = diff(Numbers)
V = std(G)
print("Standard deviation (higher is better) of Hash (Numbers):")
print(V)
medel2 += V

G = diff(SmallL)
V = std(G)
print("Standard deviation (higher is better) of Hash (Small letters):")
print(V)
medel2 += V


G = diff(CapitalL)
V = std(G)
print("Standard deviation (higher is better) of Hash (Capital Letters):")
print(V)
medel2 += V
print("Average standard deviation for hash is:")
print(medel2/3)
