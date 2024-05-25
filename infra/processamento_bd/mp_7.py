# Pi Paralelo Value

import time
from multiprocessing import Process, Queue

procs = 6
sums = Queue()

def pi_p(start, end, step, sums):
    print ("Start: ", str(start))
    print ("End: ", str(end))
    sum = 0.0
    for i in range(start, end):
        x = (i+0.5) * step
        sum = sum + 4.0/(1.0+x*x)
    sums.put(sum)

if __name__ == "__main__":
    num_steps = 100000000 #8
    sum = 0.0
    step = 1.0/num_steps
    proc_size = num_steps // procs
    workers = []
    tic = time.time()
    for i in range(procs):
        worker = Process(target=pi_p, args=(i*proc_size, (i+1)*proc_size-1, step, sums, ))
        workers.append(worker)
    for worker in workers:
            worker.start()
    for worker in workers:
            worker.join()
    toc = time.time()

    for i in range(sums.qsize()):
        sum += sums.get()
    pi = step * sum
    print('Valor de pi: %.20f' %pi)
    print('Tempo de pi %.8f' %(toc-tic))
