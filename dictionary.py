import random

a = random.randint(100, 999)
src_a = {'key_1': a}
b = random.randint(100, 999)
src_b = {'key_2': b}
c = random.randint(100, 999)
src_c = {'key_3': c}


def summary(src_a, src_b, src_c):
    src_x = {**src_a, **src_b, **src_c}
    print(src_x)


summary(src_a, src_b, src_c)
