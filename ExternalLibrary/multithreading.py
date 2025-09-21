import threading
import time
from concurrent.futures import ThreadPoolExecutor

def fun(sleeps):
    print(f"function sleeps for {sleeps}")
    time.sleep(sleeps)
    return sleeps

def main():
    time1=time.perf_counter()
    # function without threading
    # fun(4)
    # fun(2)
    # fun(1)

    # with threading
    t1=threading.Thread(target=fun,args=[4])
    t2=threading.Thread(target=fun,args=[2])
    t3=threading.Thread(target=fun,args=[1])

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    time2=time.perf_counter()
    print(time2-time1)

# with concurrent futures
def concurrentDemo():
    with ThreadPoolExecutor() as executor:
        # future1= executor.submit(fun,3)
        # future2= executor.submit(fun,2)
        # future3 = executor.submit(fun,5)
        # print(future1.result())
        # print(future2.result())
        # print(future3.result())
        list=[3,2,1,5]
        results=executor.map(fun,list)
        for result in results:
            print(result)

concurrentDemo()



