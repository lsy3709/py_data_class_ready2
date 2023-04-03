# outFp = None
# outStr=""

# outFp = open("test2.txt","w")

# while True:
#   outStr = input("내용 입력: ")
#   if outStr != "":
#     outFp.writelines(outStr + "\n")
#   else:
#     break

# outFp.close()
# print("정상 파일 씀.")


#윈도우즈로 확인하기.
inFp, outFp = None, None 
inStr = ""

inFp = open("C:/Windows/win.ini", "r")
outFp = open("C:/Temp/data3.txt", "w")

inList = inFp.readlines()
for inStr in inList :
    outFp.writelines(inStr)

inFp.close()
outFp.close()
print("--- 파일이 정상적으로 복사되었음 ---")
