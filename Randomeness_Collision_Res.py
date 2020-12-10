import bcrypt
from aus_func import generate_passwords,unique_values,modlus_str

salt = bcrypt.gensalt(6)

# test the collision for an index generation (modlus of numbers)
# This also a test for Randomness

# generate Random strings or numbers then convert to strings
K = 1000
N = K
Random_Passwords = generate_passwords(K)  # K = 1000 value only

# hash 
L = [hash(r) % N for r in Random_Passwords]
G = unique_values(L)
D = G/K  # how much is unique at all
print("Hash created {0}% Of the {1} Numbers group".format(int(D*100), N))

# bcrypt
L = [modlus_str(bcrypt.hashpw(r, salt), N) for r in Random_Passwords]
G = unique_values(L)
D = G/K  # how much is unique at all
print("Bcrypt created {0}% Of the {1} Numbers group".format(int(D*100), N))

# modlus_str : start with heaviest digit
# calculate the mod on N, then multiply by it number of digit (ten power)
# lastly add the result to the next one
# using ord.

