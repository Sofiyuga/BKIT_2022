from time import sleep, time
from contextlib import contextmanager


class cm_timer_1:
    def __int__(self):
        self.__start = 0
        self.__finish = 0

    def __enter__(self):
        self.__start = time() 

    def __exit__(self, exp_type, exp_value, traceback):
        self.__finish = time()
        print(f'Time of work: {self.__finish - self.__start}')


@contextmanager
def cm_timer_2():
    start = time()
    yield None
    finish = time()
    print(f'Time of work: {finish - start}')
