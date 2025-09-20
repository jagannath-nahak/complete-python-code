import asyncio
import time
import requests

async def fun1():
    url="https://www.bing.com/th/id/OIP.jhWWQp64YEzqQ9K0fMcLBAHaEK?w=245&h=211&c=8&rs=1&qlt=70&r=0&o=7&cb=thws5&dpr=1.3&pid=3.1&rm=3"
    response=requests.get(url)
    open("picture1.jpg","wb").write(response.content)
    print("function 1")
    return "harry"

async def fun2():
    url="https://www.bing.com/th/id/OIP.aL9ap7kxo02xpexoOhRcEAHaEK?w=245&h=211&c=8&rs=1&qlt=70&r=0&o=7&cb=thws5&dpr=1.3&pid=3.1&rm=3"
    response=requests.get(url)
    open("picture2.jpg","wb").write(response.content)
    print("Function 2")

async def fun3():
    url="https://www.bing.com/th/id/OIP.VfqJFJtm2O47nxIJtDcuBAHaFA?w=244&h=211&c=8&rs=1&qlt=70&r=0&o=7&cb=thws5&dpr=1.3&pid=3.1&rm=3"
    response=requests.get(url)
    open("picture3.jpg","wb").write(response.content)
    print("Function 3")

async def main():
    L=await asyncio.gather(
        fun1(),
        fun2(),
        fun3()
    )
    print(L)
    # await fun1()
    # await fun2()
    # await fun3()

asyncio.run(main())