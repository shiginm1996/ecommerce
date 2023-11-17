# Assignment 3
# def cube():
#     n = int(input('enter a number'))
#     print('cube of %d\t=\t%d'%(n,(n**3)))
# cube()
#
#
#
# x=lambda b,h:1/2*b*h
# b=int(input('enter the base value'))
# h=int(input('enter the height'))
# print('Area of Triangle;')
# print(x(b,h))



# def largest(li):
#   print('li=',li)
#   li.sort()
#   return li[-2]
# li=[5,6,9,7,30,2,3,4,32,12]
# print('second largest number=',largest(li))


# def dicfun(word):
#     dic = {}
#
#     for i in word:
#         if i in dic:
#             dic[i] += 1
#         else:
#             dic[i] = 1
#
#     print(dic)
# word=input('enter a word')
# dicfun(word)


# def fib(num):
#     a=0
#     b=1
#     print('fibonacci series of n=%d are;'%num)
#     for i in range(num):
#         print(a)
#         c=a+b
#         a=b
#         b=c
#
# num=int(input('enter a number'))
# fib(num)


# def val(*a):
#     m=1
#     for i in a:
#         m*=i
#     print(m)
# val(1,2,3,4,5)

# def largest_tax(*s):
#     lartax=0
#     for i in s:
#         if i>100000:
#             tax=i*(10/100)
#             print('tax for salary %d=%d'%(i,tax))
#         elif i>50000 and i<=100000:
#             tax=i*(5/100)
#             print('tax for salary %d=%d' % (i, tax))
#         elif i>20000 and i<=50000:
#             tax=i*(2/100)
#             print('tax for salary %d=%d' % (i, tax))
#
#         if lartax<tax:
#             lartax=tax
#         print()
#     print('Highest Tax=',lartax)
#
# largest_tax(120000,80000,30000)



# assignment 4
# 1

# n=int(input('enter a number'))
# a=n
# s=0
# while(n!=0):
#     rem=n%10
#     s+=rem
#     n=n//10
# print('sum of digits of %d=%d'%(a,s))



# 2
# i=1
# f=1
# n=int(input('enter the number'))
# while(i<=n):
#     f*=i
#     i+=1
# print('factorial of %d=%d'%(n,f))


# Q3
# n=int(input('enter a number'))
# sam=n
# i=1
# rev=0
# while(n!=0):
#     rem=n%10
#     rev=rev*10+rem
#     n=n//10
#     i+=1
# if sam==rev:
#     print('%d is palindrome'%sam)
# else:
#     print('%d is not palindrome'%sam)


# Q4
# p=0
# ne=0
# while(True):
#     n=int(input('enter a number'))
#     if n>0:
#         p+=n
#     elif n<0:
#         ne+=n
#     else:
#         break
# print('sum of positive=',p)
# print('sum of negative=',ne)

# Q5
# word=input('enter a word')
# rev=''
# l= len(word)
# i=l-1
# while(i>=0):
#     rev+=word[i]
#     i-=1
# print(rev)

# Q6
# a=int(input('enter a '))
# b=int(input('enter b'))
# print(' 1.Addition\n','2.Substraction\n','3.Multiplication\n','4.Division')
# choice=int(input('select a choice='))
# while (choice<=4):
#     if choice==1:
#         print('Result:\n%d+%d=%d'%(a,b,a+b))
#         break
#     elif choice==2:
#         print('Result:\n%d-%d=%d'%(a,b,a-b))
#         break
#     elif choice==3:
#         print('Result:\n%d*%d=%d'%(a,b,a*b))
#         break
#     elif choice==4:
#         print('Result:\n%d/%d=%f'%(a,b,a/b))
#         break
#     else:
#         print('Result:\nError')
#         break





