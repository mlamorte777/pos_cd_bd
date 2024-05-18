from multiprocessing import Process

def f(name):
    print('hello, sou o', name)

if __name__ == '__main__':
    p = Process(target=f, args = ('Mikael', ))
    p.start()
    p.join()

