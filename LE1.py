num1 = input("coeffs x:")
num2 = input('coeffs y:')
num3 = input('coeffs x:')
num4 = input('coeffs y:')
z1 = input('z1:')
z2 = input('z2:')
if num1 != num3:
  d = float(num3)/float(num1)
  num1 = float(num1) * d
  num2 = float(num2) * d
  z1 = float(z1) * d
  print(num1,num2,z1,num3)
if float(num1) == float(num3):
  a =float(num2) - float(num4)
  b =float(z1) - float(z2)
  c = b/a
  print("y:",c)
  print('x:',float(z1)-float(c))  
