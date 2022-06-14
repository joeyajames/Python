d=1
while d!=5:
 print("Menu\n1.ADD\n2.SUB\n3.MUL\n4.DIV\n5.Exit\n")
 d=int(input("Enter the Option : "))
 if d!=5:
  a=int(input("Enter the Num1 : "))
  b=int(input("Enter the Num2 : "))
 if d==1:
     print(a+b)
 elif d==2:
     print(a-b)
 elif d==3:
     print(a*b)
 elif d==4:
     print(a/b)
