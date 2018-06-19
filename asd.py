import time
import multiprocessing

#why it uses the all four cores?

def hayda():
    #print("Calculating square")
    while(True):
        print("Hayda")
        #time.sleep(0.01)


if __name__ == "__main__" :
    p1 = multiprocessing.Process(target=hayda,args=())
    p2 = multiprocessing.Process(target=hayda,args=())

    p1.start()
    p2.start()

    p1.join()
    p2.join()