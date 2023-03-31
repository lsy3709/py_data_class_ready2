# inFp = None 
# inStr = ""

# inFp = open("test1.txt","r")

# inStr = inFp.readline()
# print(inStr, end="")
# print("")

# inStr = inFp.readline()
# print(inStr, end="")
# print("")

# inStr = inFp.readline()
# print(inStr, end="")
# print("")

# inFp.close()


inFp = None 
inStr = ""

inFp = open("test1.txt","r")

while True :
  inStr = inFp.readline()
  if inStr == "" :
    break
  print(inStr,end="")

inFp.close()