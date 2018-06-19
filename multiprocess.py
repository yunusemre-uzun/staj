import time
import multiprocessing

def calc_square(numberlist):
    #print("Calculating square")
    for i in range(len(numberlist)) :
        time.sleep(0.2)
        print("Squre:" + str(numberlist[i]*numberlist[i]))
        numberlist[i] = int(numberlist[i]*numberlist[i])

def calc_cube(numberlist):
    #print("Calculating cube")
    for i in range(len(numberlist)) :
        time.sleep(0.2)
        print("Cube:" + str(numberlist[i]*numberlist[i]*numberlist[i]))
        numberlist[i] = int(numberlist[i]*numberlist[i]*numberlist[i])


if __name__ == "__main__" :
    numberlist = input().split(',')
    for i in range(len(numberlist)) :
        numberlist[i] = int(numberlist[i])
    t = time.time()
    p1 = multiprocessing.Process(target=calc_square,args=(numberlist,))
    p2 = multiprocessing.Process(target=calc_cube,args=(numberlist,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    print("Calced in :" + str(time.time()-t))
    print(numberlist)

