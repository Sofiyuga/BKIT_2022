import random
def gen_random(num_count, begin, end):
    for i in range(0, num_count):
        yield random.randint(begin, end)



