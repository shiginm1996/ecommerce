# def add(a,b):
#     print(a+b)
# add(1,2)
# add(1025,2546)
# def add(a,b):
#     print(a+b)
# num1=int(input('enter the number'))
# num2=int(input('second number'))
# add(num1,num2)
# Q.find factorial
# def fact(a):
# num=int(input('enter the number'))
#     f=1
#     for i in range(1,a+1):
#         f*=i
#     print(f)
# num=int(input('enter the number'))
# fact(num)
# find largest of 3 numbers using functin with argument
# def largest(a,b,c):
#     if a>b and a>c:
#         print('%d is the largest'%a)
#     elif b>c:
#         print('%d is the largest'%b)
#     else:
#         print('%d is the largest'%c)
# num1=int(input('enter the number1'))
# num2=int(input('enter the number1'))
# num3=int(input('enter the number1'))
# largest(num1,num2,num3)
# Q.reverse of string using function arg
# def rev(n):
#     print(n[::-1])
# word=input('enter a word')
# rev(word)
# find a number is amstrong using function arg
# def amstr(a):
#     armstrong=0
#     b=a
#     while a!=0:
#         reminder=a%10
#         armstrong+=reminder**3
#         a//=10
#     if b==armstrong:
#         print('armstrong')
#     else:
#         print('not armstrong')
# n=int(input('enter a number'))
# amstr(n)
# def rev(a):
#     re=0
#     for i in range(0,num+1):
#         rem=a%10
#         re=(re*10)+rem
#         a//=10
#     print(re)
# num=int(input('enter a number'))
# rev(num)
# reverse of a number with function
# def rev(a):
#     re=0
#     while a!=0:
#         rem=a%10
#         re=(re*10)+rem
#         a//=10
#     print(re)
# num=int(input('enter a number'))
# rev(num)
# area of circle
# def area(r):
#     pie=3.14
#     ar=pie*(r**2)
#     print(ar)
# r=int(input('enter the radius'))
# area(r)
# quadratic
# def quadratic(a,b,c):
#     sol1=((-b+((b**2)-(4*a*c))/(2*a)))
#     sol2=((-b-((b**2)-(4*a*c)))/(2*a))
#     print(sol1)
#     print(sol2)
# num1=int(input('enter the first'))
# num2=(int(input('enter the second')))
# num3=int(input('enter the third'))
# quadratic(num1,num2,num3)
# quadratic
# a=int(input('enter a'))
# b=int(input('enter b'))
# c=int(input('enter c'))
# d=((b**2)-(4*a*c))**0.5
# x1=(-b+d)/(2*a)
# x2=(-b-d)/(2*a)
# print(x1)
# print(x2)
# quadratic using function
# def quadratic(a,b,c):
#     d=((b**2)-(4*a*c))**0.5
#     x1=(-b+d)/(2*a)
#     x2=(-b-d)/(2*a)
#     print(x1)
#     print(x2)
# num1=int(input('enter the number'))
# num2=int(input('enter the second number'))
# num3=int(input('enter the third number'))
# quadratic(num1,num2,num3)
# 08-05-23
# Q1 road tax
# >100000   15%
# >50000 and <=100000     10%
# <=50000        5%
# def tax(cost):
#     if cost>100000:
#         t=cost*15/100
#     elif cost>50000 and cost<=100000:
#         t=cost*10/100
#     else:
#         t=cost*5/100
#     print(t)
# c=float(input('enter the cost'))
# tax(c)
# Q2 devisible by 2 and 3
# def div(n):
#     if n%2==0 and n%3==0:
#         print('devisible by 2 and 3')
#     else:
#         print('not devisible by 2 and 3')
# num=int(input('enter the number'))
# div(num)
# Q3:bonus
# def bonus(sal,exp):
#     if exp>10:
#         b=sal*10/100
#     elif exp>=6 and exp<=10:
#         b=sal*8/100
#     else:
#         b=sal*5/100
#     print(b)
# s=float(input('enter the salary'))
# y=int(input('enter the year of experience'))
# bonus(s,y)




























