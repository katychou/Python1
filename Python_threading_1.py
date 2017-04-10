#Python_threading
#2.add thread
'''
import threading

def thread_job():
      print('This is an added Thread, number is %s'%threading.current_thread())

def main():
      added_thread=threading.Thread(target=thread_job)
      added_thread.start()
      print(threading.active_count())
      print(threading.enumerate())
      #MainThread(MainThread, started 6680)>, <Thread(SockThread, started daemon 3896)>]
      print(threading.current_thread())
      

if __name__=='__main__':
      main()
'''
#3.join
'''
import threading
import time

def thread_job():
      print('T1 start\n')
      for i in range(10):
            print(i)
            time.sleep(0.1)
      print('T1 finish\n')
      
def T2_job():
      print('T2 start\n')
      print('T2 finish\n')

def main():
      added_thread=threading.Thread(target=thread_job,name='T1')
      added_thread2=threading.Thread(target=T2_job,name='T2')
      added_thread.start()
      added_thread2.start()
      added_thread.join()
      added_thread2.join()
      print('all done!\n')

if __name__=='__main__':
      main()
'''

#4.Queue
#threading no return vlaue, need input to queue
'''
import threading
import time
from queue import Queue

def job(l,q):
      for i in range(len(l)):
            l[i]=l[i]**2
      q.put(l)

def multithreading():
      q=Queue()
      threads=[]        #all threading input the threads[] list
      data=[[1,2,3],[3,4,5],[4,4,4],[5,4,3,2]]
      for i in range(4):
            t=threading.Thread(target=job,args=(data[i],q))
            t.start()
            threads.append(t)
      for thread in threads:        #every thread add to main_thread
            thread.join()
      results=[]        #init :null list
      for _ in range(4):
            results.append(q.get())     #from queue get a value
      print(results)
                              
if __name__=='__main__':
      multithreading()

'''
#5.GIL-GlobalInterpreterLock
'''
import threading
from queue import Queue
import copy
import time

def job(l, q):
    res = sum(l)
    q.put(res)

def multithreading(l):
    q = Queue()
    threads = []
    for i in range(4):
        t = threading.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
        t.start()
        threads.append(t)
    [t.join() for t in threads]
    total = 0
    for _ in range(4):
        total += q.get()
    print(total)

def normal(l):
    total = sum(l)
    print(total)

if __name__ == '__main__':
    l = list(range(1000000))
    s_t = time.time()
    normal(l*4)         #WAY1-normal
    print('normal: ',time.time()-s_t)
    s_t = time.time()
    multithreading(l)   #WAY2-multithreading
    print('multithreading: ', time.time()-s_t)
'''
#6.Lock
import threading

def job1():
      global A,lock
      lock.acquire()
      for i in range(10):
            A+=1
            print('job1',A)
      lock.release()
      
def job2():
      global A,lock
      lock.acquire()
      for i in range(10):
            A+=10
            print('job2',A)
      lock.release()

if __name__=='__main__':
      lock=threading.Lock()
      A=0
      t1=threading.Thread(target=job1)
      t2=threading.Thread(target=job2)
      t1.start()
      t2.start()
      t1.join()
      t2.join()



    



