inFp = None	# 입력 파일
inList = []
inStr = ""		# 읽어온 문자열
lineNum = 1

with open("test1.txt","r") as inFp :
# inFp = open("test1.txt","r")
# inFp = open("C:/Temp/data1.txt", "r", encoding="utf-8" )
#inFp = open("C:/Temp/data1.txt", "r")

# while True :
#     inStr = inFp.readline()
#     if inStr == "" :
#         print("")
#         break;
#     print("%d : %s" %(lineNum, inStr), end="")
#     lineNum += 1

    inList = inFp.readlines()
print(inList)

for inStr in inList:
   print("%d : %s" % (lineNum,inStr), end="")
   lineNum += 1

# inFp.close()
