import time
import multiprocessing

#why it uses the all four cores?

def hayda1(x):
    #print("Calculating square")
    while(True):
        x = x+1
        print("hayda1:"+str(x))
        time.sleep(0.2)

def hayda2(x):
    #print("Calculating square")
    while(True):
        x = x+1
        print("hayda2:"+str(x))
        time.sleep(0.2)


if __name__ == "__main__" :
    x = int(input())
    p1 = multiprocessing.Process(target=hayda1,args=(x,))
    p2 = multiprocessing.Process(target=hayda2,args=(x,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()