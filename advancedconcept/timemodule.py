import time

# def useWhile():
#     i=0
#     while i<1000:
#         i=i+1
#         print(i)

# def useFor():
#     for i in range(1000):
#         print(i)


# init=time.time()
# useWhile()
# t1=time.time()-init
# init=time.time()
# useFor()
# print(time.time()-init)
# print(t1)

# it is used to pending the execution of program
# print(4)
# time.sleep(4)
# print("Hello, I am time")


# it gives us local time

t=time.localtime()
formatted_time=time.strftime("%Y-%m-%d %H:%M:%S",t)

print(formatted_time)


