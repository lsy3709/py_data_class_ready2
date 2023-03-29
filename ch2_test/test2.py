a = int(100.0)
print(a)

## 주석. 

'''
여러줄 주석 
'''

b = 'hi' + \
  'hi2' + \
    'hello'
print(b)

def sumA(a,b):
  result = a + b
  print(a, "+", b, "=", result)
  result = a - b
  print(a, "-", b, "=", result)
  result = a * b
  print(a, "*", b, "=", result)
  result = a / b
  print(a, "/", b, "=", result)

sumA(10,20)
