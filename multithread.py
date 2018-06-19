import time
import threading

#different times in sleeps creates different outputs why?
# an error in a thread does not interrupt the other thread

numberlist = input().split(',')
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
for i in range(len(numberlist)) :
   numberlist[i] = int(numberlist[i])
t = time.time()
t1 = threading.Thread(target=calc_square,args=(numberlist,))
t2 = threading.Thread(target=calc_cube,args=(numberlist,))

t1.start()
t2.start()

t1.join()
t2.join()

print("Calced in :" + str(time.time()-t))
print(numberlist)