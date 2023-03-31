outFp = None
outStr=""

outFp = open("test2.txt","w")

while True:
  outStr = input("내용 입력: ")
  if outStr != "":
    outFp.writelines(outStr + "\n")
  else:
    break

outFp.close()
print("정상 파일 씀.")