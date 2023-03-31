import random

imageTuple = ()
value = 1
ROW = COL = 3
tt= ((1,2,3),(4,5,6),(7,8,9))
if __name__ =="__main__":
    for i in range(0, ROW):
        for k in range(0,COL):
            print("%d" % tt[i][k],end=" ")
        print("")
        