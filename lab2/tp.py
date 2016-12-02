import time
import random
from time import sleep


class timer:
    def __enter__(self):
        time.clock()
        return self

    def __exit__(self, *args):
        print(time.clock())
    def time_passed(self):
        return(time.clock)


with timer() as t:
    for _ in range(10):
        sleep(random.random())
        print(t.time_passed())