constant_a = 75
constant_c = 74
M = 2**16+1
seed = 3
for i in range(100):
    modulus = (constant_a * seed + constant_c)
    while modulus >= M or modulus == M:
            modulus -= M

    remainder = modulus
    seed = remainder
    while remainder >= 10:
        remainder -= 10
    print(remainder)




