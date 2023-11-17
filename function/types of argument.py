# default
# def add(a,b=1):
#     print(a+b)
# add(5)
# b is default value.so we give a as input.if we gave both values a=2,b=3, b will changed from  to 3
# def add(a,b=1):
#     print(a+b)
# add(5,6)
# Q
# multiply(1,2)
# multiply(1,2,3)
# multiply(1,2,3,4)
# def mult(a=1,b=1,c=1,d=1):
#     print(a*b*c*d)
# mult(1,2)
# mult(1,2,3)
# mult(1,2,3,4)
# Q
# largest1,2
# largest1,2,3
# largest1,2,3,4
# def lar(a,b,c=0,d=0):
#     if a>b and a>c and a>d:
#         print('%d is largest'%a)
#     elif b>c and b>d:
#         print('%d is the largest'%b)
#     elif c>d:
#         print('%d is largest'%c)
#     else:
#         print('%d is the largest'%d)
# lar(1,2)
# lar(1,2,3)
# lar(1,2,3,4)
# note:why we give 0 to last two parameters is bcz we need atleast 2 parameters for copmarison others treated as input values


# keyword argumnet
# def name(first_name,middle_name,last_name):
#     print(first_name,middle_name,last_name)
# name(middle_name='shigin',first_name='arun',last_name='joju')
# arbitary argumnet
# def val(*a):
#     print(a)
# val(1,2,3,4,5)
# note:we will get tuple
# how to visit each value
# def val(*a):
#     s=0
#     for i in a:
#         s+=i
#     print(s)
# val(1,2,3,4,5)
# val(1,2,3,4,5,6)
# multiply
# def val(*a):
#     m=1
#     for i in a:
#         m*=i
#     print(m)
# val(1,2,3,4,5)
# val(1,2,3,4,5,6)
# val(1,2,3)
#
#
# largest of numbers using arbitary function
# def largest(*a):
#     b=0
#
#     for i in a:
#         if i>b:
#             b=i
#     print('%d is the largest'%b)
# largest(2,5,15,7,9)
# largest(25,15,8,75,2)
# largest(250,45,75,14,65,500)
# 09-05-23
# def name(**a):
#     for i,j in a.items():
#         print(i,j)
# name(first_name='shigin',last_name='M',phone_no=9747806171)
# #we will get dictionery,so will changed in to single values by iteration






