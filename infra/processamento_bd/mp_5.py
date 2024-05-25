# Pipe

import time
from multiprocessing import Process, Pipe

procs = 6
a,b = Pipe()

def pi_p(start, end, step, sums):
    print ("Start: ", str(start))
    print ("End: ", str(end))
    sum = 0.0
    for i in range(start, end):
        x = (i+0.5) * step
        sum = sum + 4.0/(1.0+x*x)
    sums.send(sum)

if __name__ == "__main__":
    num_steps = 1000000000
    sum = 0.0
    step = 1.0/num_steps
    proc_size = num_steps // procs
    workers = []
    tic = time.time()
    for i in range(procs):
        worker = Process(target=pi_p, args=(i*proc_size, (i+1)*proc_size-1, step, a, ))
        workers.append(worker)
    for worker in workers:
            worker.start()
    for worker in workers:
            worker.join()
    toc = time.time()

    for i in range(procs):
        sum += b.recv()
    pi = step * sum
    print('Valor de pi: %.20f' %pi)
    print('Tempo de pi %.8f' %(toc-tic))
