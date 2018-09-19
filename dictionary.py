import random

src_a = dict(key_1=(random.randint(100, 999)))
src_b = dict(key_2=(random.randint(100, 999)))
src_c = dict(key_3=(random.randint(100, 999)))


def summary(src_a, src_b, src_c):
    src_x = {**src_a, **src_b, **src_c}
    print(src_x)


summary(src_a, src_b, src_c)
