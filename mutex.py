import threading,time
l=threading.Lock()
s=threading.Semaphore(2)
def myfunc():
    i=0
    l.acquire()
    while i<20:
        print(f"{threading.get_native_id()}:: ",i)
        i+=1
        print(l.locked())
    l.release()
    print(l.locked())
    print("*"*100)

for item in range(3):
    threading.Thread(target=myfunc).start()
