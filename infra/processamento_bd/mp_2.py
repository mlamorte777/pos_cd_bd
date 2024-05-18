from multiprocessing import Process

def f(name, id):
    print('hello, sou', name, id)

if __name__ == '__main__':
    procs = []
    num = 6
    for i in range(num):
        p = Process(target=f, args=('bob filho', i, ))
        procs.append(p)

print('hello, sou', 'bob pai')
for i in range(num):
    procs[i].start()
for i in range(num):
    procs[i].join()