# print("hi")
# print("%d" % 100)
# print("%d" % (100*9))

# def myFunc():
#   print("hi")

# gVar = 100 

# if __name__ == '__main__' :
#   print("메인 함수 실행 됨.")
#   myFunc()
#   print("전역 변수 값: ",gVar)  

# a = 100; b = 100.123
# c= str(a)+'1'
# d= str(b)+'1'
# print(c,d)

# if(1234): print("참 보임")
# if(0) : print("거짓 안 보임")

# ## 변수 선언 부분 ##
# money, c50000, c10000, c5000, c1000 = 0, 0, 0, 0, 0

# ## 메인 코드 부분 ##
# money=int(input("교환할 돈은 얼마 ? "))

# c50000 = money // 50000
# money %= 50000

# c10000 = money // 10000
# money %= 10000

# c5000 = money // 5000
# money %= 5000

# c1000 = money // 1000
# money %= 1000

# print("\n 50000원짜리 ==> %d장" % c50000)
# print(" 10000원짜리   ==> %d장 " % c10000)
# print(" 5000원짜리 ==> %d장 " % c5000)
# print(" 1000원짜리   ==> %d장 " % c1000)
# print(" 바꾸지 못한 잔돈 ==> %d원" % money)

# a = 200 

# if a < 100 :
#     print("100보다 작네")
# else :
#     print("100보다 크네")    

# a = int(input("정수를 입력하세요: "))

# if a % 2 == 0 :
#   print("짝수")

# else :
#   print("홀수")
  
# a = 15

# if a > 50 :
#     if a < 100 :
#       print("50보다 크고 100보다 작다")
#     else :
#       print("100보다 크다.")
# else :
#   print("100보다작다.") 

# score = int(input("점수를 입력하세요 : "))

# if score >= 90 :
#     print("A")
# else :
#     if score >= 80 :
#       print("B")
#     else :
#       if score >= 70 :
#         print("C")
#       else :
#         if score >= 60 :
#           print("D")
#         else :
#           print("F")
# print("학점임.")

# score = int(input("점수를 입력하세요 : "))

# if score >= 90 :
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")    
# else :
#     print("F")
# print("학점임.")    

# score = int(input("점수를 입력하세요 : "))

# if score >= 90 :
#     print("A+")
# elif score >= 85:
#     print("B+")
# elif score >= 80:
#     print("B")
# elif score >= 75:
#     print("C+")   
# elif score >= 70:
#     print("C0")   
# elif score >= 65:
#     print("D+")   
# elif score >= 60:
#     print("D0")               
# else :
#     print("F")
# print("학점임.")   

# import random

# numbers = []

# for num in range(0,10) :
#   numbers.append(random.randrange(0,10))

# print("생성된 리스트", numbers)

# for num in range(0, 10) :
#   if num not in numbers :
#     print("숫자 %d는(은) 리스트에 없음" % num)  

# select, answer, numStr, num1, num2 = 0, 0, "", 0,0

# select = int(input("1. 입력한 수식 계산  2. 두 수 사이의 합계 : "))

# if select == 1 :
#   numStr = input("*** 수식을 입력하세요 : ")
#   answer = eval(numStr)
#   print(" %s 결과는 : %5.1f 입니다." % (numStr, answer))
# elif select == 2 :
#   num1 = int(input("*** 첫 번째 숫자를 입력하세요 : "))  
#   num2 = int(input("*** 두 번째 숫자를 입력하세요 : "))  
#   for i in range(num1, num2 + 1) :
#     answer = answer + i 
#   print("%d+...+%d는 %d 입니다." % (num1, num2, answer))
# else :
#   print("1 또는 2만 입력해야 함.")    

# select, answer, numStr, num1, num2, num3 = 0, 0, "", 0,0,0

# select = int(input("1. 입력한 수식 계산  2. 두 수 사이의 합계 : "))

# if select == 1 :
#   numStr = input("*** 수식을 입력하세요 : ")
#   answer = eval(numStr)
#   print(" %s 결과는 : %5.1f 입니다." % (numStr, answer))
# elif select == 2 :
#   num1 = int(input("*** 첫 번째 숫자를 입력하세요 : "))  
#   num2 = int(input("*** 두 번째 숫자를 입력하세요 : "))  
#   num3 = int(input("*** 증가 할 숫자를 입력하세요 : "))  
#   for i in range(num1 , num2 + 1, num3) :
#     answer = answer + i 
#   print("%d+...+%d는 %d 입니다." % (num1, num2, answer))
# else :
#   print("1 또는 2만 입력해야 함.") 
  
# for i in range(0,9,2) :
#   print("hi"+str(i))  

# for i in range(1,6,1):
#   print("%d " % i, end="===")
  
  
# hap = 0
 
# for i in range(0,101,7):
#    hap = hap + i 
# print("0 ~ 100 사이에 있는 7의 배수 합계 : %d" % hap)    
  
# for i in range(0,3,1) :
#   for k in range(0,2,1) :
#     print("hi~(i값 : %d, k값 : %d)" % (i,k))
  
# for i in range(2,10,1) :
#   print("## %d단##" % i)
#   for k in range(1,10,1) :
#     print(i,"X",k,"=",i*k)
#   print()  
# i = 0
# while i < 3 :
#   print("hi")
#   i = i + 1

# i, hap  = 0,0

# # i = 1 
# while i < 11 :
#   hap = hap + i 
#   i = i + 1
# print("1에서 10까지의 합계 : %d" % hap)

# while True :
#   print("ㅋ ", end=" ")

# hap , a, b = 0,0,0 

# while True :
#   a = int(input("더할 첫 번째 수를 입력하기 : "))
#   if a == 0 :
#     break
#   b = int(input("더할 두 번째 수를 입력하기 : "))
#   hap = a + b 
#   print("%d + %d = %d" % (a,b,hap))

# print("0을 입력해 반복문 탈출 가능.")

# hap, i = 0,0 

# for i in range(1,101) :
#   if i % 3 ==0 :
#     continue
  
#   hap +=i 
# print(" 1~ 100 의 합계(3의 배수 제외) : %d" % hap)

# print("%04d" % 876)
# print("%s" % "CookBook")
# print("%6.1f" % 123.45)

# num = 100
# num += 1
# num -= 1
# num *= 1
# num /= 1
# num = int(num)
# print(num)

# num = 0 
# if num > 0 :
#   print("케이스1", end=' ')
# else :
#   print("케이스2", end=' ')
# print("케이스3", end=' ')  

# num = int(input("정수 : "))

# if not num % 5 == 0 :
#   print("5의 배수가 아님.")
# else :
#   print("5의 배수")  

# score = int(input("점수를 입력 하세요: "))

# if score >= 90 :
#   print("장학생",end=' ')
# elif score >= 60 :
#   print("합격", end='')
# else :
#   print("불합격", end='')    
# print("입니다.")    

# for i in range(5,0,-1):
#   print("%d" % i)

# sum = 0

# for i in range(3333,9999):
#   if i % 1234 == 0 :
#     continue
    
#   elif i % 1234 !=0 :
#     sum = sum + i 
#     if sum > 100000 :
#       sum -= i
#       break
   
# print(sum)  
import math
import copy 

# n = math.sqrt(101)

# 맨앞에 추가 하기. 
# list.insert(0, 'a')



# def removeMultiNum(a, n) :
#   for i in a:
#     if i % n == 0 :
#       a.removie(i)
#   return a
      

# print(a)  
# 2의 배수 빼고 남은 a 
# b = copy.deepcopy(a)

# a = []
# b = []

# for i in range(3,101) :
#   if i % 2 != 0 :
#     a.append(i)
    
# print(a)
# print(len(a))
# # 3의 배수 빼기. 
# for k in a:
#    if k % 3 == 0 :
#      a.remove(k)

# for i in a:
#   if i % 5 == 0 :
#     a.remove(i)

# for i in a:
#   if i % 7 == 0 :
#     a.remove(i)

# b = [ 3, 5, 7]
    
# a.extend(b)
# a.sort()
# print(a)
# print(len(a))

# 소수 구하기 이중 for 문, 
# 2를 제외한 3부터 해서 해당 범위 안에 값으로 나누어 지면 
# 안에 반복문 빠져 나가고, 아니면 해당 리스트에 추가하기. 
primes = []
for num in range(3, 10000):
    for i in range(2, num):
        if (num % i) == 0:
            break
    else:
      primes.append(num)
    
print(primes)
print(len(primes))