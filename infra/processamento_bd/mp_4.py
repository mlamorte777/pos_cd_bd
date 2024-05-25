from multiprocessing import Process
import time
procs = 3

# Pi Paralelo
def pi_p(start, end, step):
    print("Start: ", str(start))
    print("End: ", str(end))
    sum = 0.0
    for i in range(start, end):
        x = (i+0.5) * step
        sum = sum + 4.0/(1.0+x*x)
    print(sum)

if __name__ == '__main__':
    num_steps = 10_000_000_00
    sums = 0.0
    step = 1.0/num_steps
    proc_size = num_steps // procs
    workers = []
    tic = time.time()
    for i in range(procs):
        worker = Process(target=pi_p, args=(i*proc_size, (i+1)*proc_size-1, step, ))
        workers.append(worker)
    for worker in workers:
        worker.start()
    for worker in workers:
        worker.join()
    toc = time.time()

    print('Tempo Pi: %.8f s' %(toc-tic))


