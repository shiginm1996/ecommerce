# def hello():
#     return 'hello'
# print(hello())
# Q write a pgrm to multiply two numbers using function with arg and return
# def mult(a,b):
#     m=a*b
#     return m
# print(mult(1,2))
# print(mult(3,5))
# Q find a number odd or even using function with arg and return
# def oe(n):
#     if n%2==0:
#         return('%d is even'%n)
#     else:
#         return('%d is odd'%n)
# print(oe(5))
# print(oe(2))
# Qsimple calculator
# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mult(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# print('simple_calculator''\noptions:','\n1.addition','\n2.subtraction','\n3.multiplication','\n4.division')
# choice=int(input('enter your choice'))
# if choice in [1,2,3,4]:
#     num1=int(input('enter the number'))
#     num2=int(input('enter the second'))
#     if choice==1:
#         print('%d + %d = '%(num1,num2),add(num1,num2))
#     elif choice==2:
#         print('%d - %d = '%(num1,num2),sub(num1,num2))
#     elif choice==3:
#         print('%d * %d = '%(num1,num2),mult(num1,num2))
#     elif choice==4:
#         print('%d - %d = '%(num1,num2),div(num1,num2))
# else:
#     print('exit')
# lamda function
# x=lambda a,b:a+b
# print(x(1,2))
# x=lambda a: 'my name is %s'%a
# print(x('shigin'))
# 10-05-2023
# Q1 solve a/b*c
# Q2 find square root of numbers
# Q3 find cube of an argumnet
# Q4mfind area of circle
# Q1
x=lambda a,b,c:(a/b)*c
a=int(input('enter the number'))
b=int(input('enter the b'))
c=int(input('enter the c'))
print(x(a,b,c))
# Q2
# x=lambda a:a**0.5
# a=int(input('enter the number'))
# print(x(a))
# q3
# x=lambda a:a**3
# a=int(input('enter the number'))
# print(x(a))
# Q4
# x=lambda a:3.14*(a**2)
# a=int(input('enter the radius'))
# print('area of circle',x(a))



