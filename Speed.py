import bcrypt
from timeit import timeit


password = b"Try this 123"
salt = bcrypt.gensalt(6)

N = 1000.0

bcrypt_speed = timeit(lambda: bcrypt.hashpw(password, salt), number=int(N))
print("bcrypt method speed (10 runs):")
print(bcrypt_speed)

hash_speed = timeit(lambda: hash(password), number=int(N))
print("Hash method speed (10 runs):")
print(hash_speed)

relative_speed = bcrypt_speed/hash_speed
print("Relative speed is (bcrypt to hash)")
print(relative_speed)

