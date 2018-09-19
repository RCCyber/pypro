import random


src_a = {'key_'+str(random.randint(1,10)): (random.randint(100, 999))}
src_b = {'key_'+str(random.randint(1,10)): (random.randint(100, 999))}
src_c = {'key_'+str(random.randint(1,10)): (random.randint(100, 999))}


def summary(src_a, src_b, src_c):
    src_x = {**src_a, **src_b, **src_c}
    print(src_x)


summary(src_a, src_b, src_c)
