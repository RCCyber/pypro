import random

a = random.randint(100, 999)
a1 = str(input("Enter the name of first key: "))
src_a = {a1: a}
b = random.randint(100, 999)
b1 = str(input("Enter the name of second key: "))
src_b = {b1: b}
c = random.randint(100, 999)
c1 = str(input("Enter the name of third key: "))
src_c = {c1: c}


def summary(src_a, src_b, src_c):
    src_x = {**src_a, **src_b, **src_c}
    print(src_x)


summary(src_a, src_b, src_c)
