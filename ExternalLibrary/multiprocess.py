import multiprocessing
import requests
import os

def downloadFiles(url,name):
    print(f"Started downloading {name}")
    response=requests.get(url)

    os.makedirs("files", exist_ok=True)

    with open(f"files/file{name}.jpg", "wb") as f:
        f.write(response.content)


    print(f"finished downloading {name}")

if __name__ == "__main__":  # ✅ Required on Windows

    url="https://picsum.photos/4000/3000"
    
    # without multiprocess
    # for i in range(10):
    #     downloadFiles(url,i)
    

    # with multiprocess
    pros=[]
    for i in range(50):
        p=multiprocessing.Process(target=downloadFiles,args=[url,i])
        p.start()
        pros.append(p)

    for p in pros:
        p.join()
