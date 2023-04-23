from queue import Queue
import queue,random
import time
from threading import Thread,Event
class Producer(Thread):
    def __init__(self,queue):
        Thread.__init__(self)
        self.queue= queue
    def run(self):
        for i in range(100):
            task=random.randint(0,256)
            print(f'Producer Notify {task} appended to queue by {self.name} \n'  )
            self.queue.put(task)
        #time.sleep(1)
class Consumer(Thread):
    def __init__(self,queue):
        Thread.__init__(self)
        self.queue=queue
    
    def run(self):
        while True:
            item=self.queue.get()
            print(f'Consumer Notify {item} poped by {self.name}' )
            self.queue.task_done()
if(__name__=='__main__'):
    queue=Queue()
    t1=Producer(queue)
    t2=Consumer(queue)
    t3=Consumer(queue)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
    