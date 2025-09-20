import functools
import time

@functools.lru_cache(maxsize=None)

def fun(n):
    time.sleep(5)
    return n*n

# it takes 5 second to execute
print(fun(5))
# it print instantly by using storing result
print(fun(5))