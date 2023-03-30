aa = []
# for i in range(0, 10) :
#     aa.append(0)
# hap = 0

# for i in range(0, 10) :
#     aa[i] = int(input(str(i+1) + "번째 숫자 : " ))

# k = 0
# while k < 10:
#   hap += aa[k]
#   k = k + 1
  
  
# #hap = aa[0] + aa[1] + aa[2] + aa[3]

# print("합계 ==> %d" % hap)

# myList = [30,10,20]
# print("현재 리스트 : %s" % myList)

# myList.append(40)
# print("append(40) 후의 리스트 : %s " % myList)

# print("pop() 으로 추출한 값 : %s " % myList.pop())
# print("pop() 후의 리스트 : %s " % myList)

# myList.sort()
# print("sort() 후의 리스트 : %s " % myList)

# myList.reverse() 
# print("reverse() 후의 리스트 : %s " % myList)

# print("20 값의 위치 : %d " % myList.index(20))
# myList.insert(2,222)

# print("insert(2,222) 후의 리스트 : %s " % myList)

# myList.remove(222)
# print("remove(222) 후의 리스트 : %s " % myList)

# myList.extend([77,88,77])
# print("extend([77,88,77]) 후의 리스트 : %s" % myList)

# print("77 값의 개수 : %d " % myList.count(77))

# list1 = []
# list2 = []
# value = 0
# for i in range(0,4):
#     for k in range(0,5):
#         list1.append(value)
#         value += 3
#     list2.append(list1)
#     list1 = []

# for i in range(0,4) :
#     for k in range(0,5):
#         print("%5d" % list2[i][k], end="")
#     print("")

import random

imageList = []
value = 0
ROW = COL = 5 

if __name__ =="__main__":
    for i in range(0, ROW):
        tmpList = [] 
        for k in range(0,COL):
            value = random.randrange(0,256)
            tmpList.append(value)
        imageList.append(tmpList)
    
    print("## 원본 2차원 배열 ## ")
    for i in range(0,ROW):
        for k in range(0,COL):
            print("%03d" % imageList[i][k], end=" ")
        print("")
    print("")
    
    for i in range(0, ROW):
        for k in range(0, COL):
            imageList[i][k] = 255 - imageList[i][k]
            
    print("## 반전된 배열 : 255 - 원래값")
    for i in range(0,ROW):
        for k in range(0,COL):
            print("%03d" % imageList[i][k], end=" ")
        print("")
    print("")