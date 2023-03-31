# ss = "파이썬은완전재미있어요"

# sslen = len(ss)
# for i in range(0,sslen):
#     if i%2 == 0 :
#         print(ss[i]  , end = '')
#     else :
        
#         print("#",end="")

# ss = '하나\n둘\n셋'
# ss2 = ss.splitlines()
# print(ss2)
# ss = '%'
# ss3 = ss.join('파이썬')
# print(ss3)

# before = ['2023','2022','2021']
# after = list(map(int,before))
# print(after)

# search = input("영어나 한글 , 숫자 특수 문자 등 각각 입력해 보기 : ")
# if search.isdigit() :
#     print("숫자입니다.")
# elif search.isalpha() :
#     print("글자입니다.")    
# elif search.isalnum() :
#     print("글자, 숫자 섞여 있습니다.")    
# else :
#     print("모르겠습니다.")    

# def calc(v1,v2,op) :
#     result = 0
#     if op == '+' :
#         result = v1 + v2 
#     elif op == '-' :
#         result = v1 - v2
#     elif op == '*' :
#         result = v1 * v2 
#     elif op == '/' :
#         result = v1/v2 
#     elif op == '**' :
#       result = v1**v2 
    
#     return result

# res = 0
# var1, var2, oper = 0,0,""      

# oper = input("계산을 입력하세요.(+,-,*,/,** : )")
# var1 = int(input("첫 번째 수를 입력 : "))
# var2 = int(input("두 번째 수를 입력 : "))

# if var2 == 0 and oper == "/":
#   print("0으로 나누면 안됩니다. ㅠㅠ-> 다시 입력 해주세요.")
# else :
#   res = calc(var1, var2, oper)
#   print("## 계산기 : %d %s %d = %d" % (var1 ,oper ,var2 , res))

# def func1() :
#   # global a 
#   a = 10 
#   print("func1() 에서 a 값 %d" % a)

# def func2() :
#   print("func2() 에서 a 값 %d" % a)

# a = 20 
# a= 30

# func1()
# func2()

# import random

# def getNumber() :
#   return random.randrange(1,46)

# lotto = []
# num = 0

# print("** 로또 추첨을 시작함 ** \n")

# while True :
#   num = getNumber() 
  
#   if lotto.count(num) == 0 :
#     lotto.append(num)
  
#   if len(lotto) >= 6:
#     break

# print("추첨된 로또 번호 ==>", end=" ")
# lotto.sort()

# for i in range(0,6) :
#   print("%d " % lotto[i], end=" ")
# print("")

# import random

# nn = []

# for _ in range(10) :
#   num = random.randrange(1,100)
#   nn.append(num)

# print(nn)
# print(len(nn))

# hap = 0

# for i in range(10) :
#   num = nn[i]
#   hap += num 
# print(hap)  

# ary1 = [1,2,3,4]
# ary2 = []
# for i in range(3,-1,-1) :
#   ary2.append(ary1[i])
# print(ary1)
# print(ary2)

# myData = [[n*m for n in range(1,3)] for m in range (2,4)]
# print(myData)

# inStr = 'IT_CookBook_Python'
# outStr = ''
# for i in range(0,len(inStr)):
#   if i%2 ==0 :
#     outStr += inStr[-(i+1)]
#   else :
#     outStr += '#'
# print("원본 내용 -->", inStr)
# print("변경 내용 -->", outStr)

# str1 = "코딩 중에서 파이썬 코딩이 가장 즐거운 코딩"
# print(str1.count('코딩'))
# print(str1.rfind('코딩'))
# print(str1.startswith('코딩'))
# print(str1.find('코딩'))


# 한글의 유니코드 십진수 범위는 4
# 4032에서 55203입니다.

# 영문 소문자: 영문 소문자의 Unicode Decimal 범위는 
# 97~122입니다.
# 이 범위에는 "a"에서 "z"까지의 영문 소문자 26개가 포함됩니다.

# 영문 대문자: 영문 대문자의 Unicode Decimal 범위는 
# 65~90입니다. 
# 이 범위에는 "A"에서 "Z"까지의 영문 대문자 26개가 포함됩니다.

# 숫자: 숫자의 유니코드 십진수 범위는 
# 48에서 57까지입니다. 
# 이 범위에는 "0"에서 "9"까지의 10자리가 포함됩니다.

# 특수 문자 기호: 문장 부호, 수학 기호, 통화 기호 등을 포함하여
# 다양한 문자를 포함하는 광범위한 범주입니다. 
# 특수 문자 기호의 유니코드 10진수 범위는 
# 32에서 126까지이며

# str = "a"
# a = ord(str)
# print(a)




# tmpU,tmpL, tmpD,tmpH, tmpE = [],[],[],[],[]

# search = input("문자열을 입력하세요 : ")

# for i in range(0,len(search)) :
#   if ord(search[i]) >= 65 and ord(search[i]) <= 90 :
#      tmpU.append(search[i])
#   elif ord(search[i]) >= 97 and ord(search[i]) <= 122 : 
#      tmpL.append(search[i])
#   elif ord(search[i]) >= 48 and ord(search[i]) <= 57 : 
#      tmpD.append(search[i])
#   elif ord(search[i]) >= 4032 and ord(search[i]) <= 55203 : 
#      tmpH.append(search[i])
#   elif ord(search[i]) >= 32 and ord(search[i]) <= 126 : 
#      tmpE.append(search[i])

# def printF(a) :
#   result = ""
#   for i in a:
#     result += i + ""
#   return result.strip()

# # for i in range(0,6) :
# #   print("%d " % lotto[i], end=" ")
# result1 = printF(tmpU)
# result2 = printF(tmpL)
# result3 = printF(tmpD)
# result4 = printF(tmpH)
# result5 = printF(tmpE)
# print("대문자 : ",result1)
# print("소문자 : ",result2)
# print("숫자 : ",result3)
# print("한글 : ",result4)
# print("기타 : ",result5)




def myFunc(p1, p2=2, p3=3):
  ret = p1 + p2 + p3
  return ret 

result = myFunc(1,7)

print("매개변수 없이 호출 안됨. 매개변수 넣어서 ==>", myFunc(1))