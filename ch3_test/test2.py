# year = 0

# if __name__ == "__main__" :
#   year = int(input("연도를 입력하세요: "))
  
#   if((year % 4 == 0) and (year % 100 !=0)) or (year % 400 ==0) :
#     print("%d년은 윤년입니다." % year)
#   else :
#     print("%d년은 윤년이 아닙니다." % year)

# 정수, 문자열 변수 정의
i, k, heartNum = 0,0,0 
numStr, ch, heartStr ="", "", ""

if __name__ == "__main__" :
    numStr = input("숫자를 여러개 입력하세요 : ")
    print("")
    i = 0
    ch = numStr[i]
    while True :
        heartNum = int(ch)
        
        heartStr = ""
        for k in range(0, heartNum):
            heartStr += "\u2665"
            k += 1 
        
        print(heartStr)
        
        i += 1
        if(i > len(numStr) - 1):
            break
        ch = numStr[i]