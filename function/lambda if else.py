# find the square of a number if number greater than 0
# x=lambda a:a**2 if a>0 else None
# print(x(5))
# note: None= Null value
# Q find a number is negative or positive using lambda
# x=lambda a:'%d is positive'%a if a>0 else '%d is negative'%a
# a=int(input('enter a number'))
# print(x(a))
#Q find largest of two numbers using lamda
x=lambda a,b:'%d is largest'%a if a>b else '%d is largest'%b
a=int(input('enter a'))
b=int(input('enter b'))
print(x(a,b))
#q convert positive to negative and negative to positive
# x=lambda a:-1*a if a>0 else -1*a
# a=int(input('enter a number'))
# print(x(a))
#Q find a number is odd orr even
# x=lambda a:'%d is even'%a if a%2==0 else '%d is odd'%a
# a=int(input('enter a number'))
# # print(x(a))
# elif
#write a pgrm to find largest of 3 numbers
# largest=lambda a,b,c:'%d is largest'%a if a>b and a>c else('%d is largest'%b if b>c else '%d is largest'%c)
# a=int(input('enter a'))
# b=int(input('enter b'))
# c=int(input('enter c'))
# print(largest(a,b,c))
# Q find smallest of three numbers
# smallest=lambda a,b,c:'%d is smallest'%a if a<b and a<c else('%d is smallest'%b if b<c else '%d is smallest'%c)
# a=int(input('enter a'))
# b=int(input('enter b'))
# c=int(input('enter c'))
# print(smallest(a,b,c))
# @write a pgrm to find negative positive or zero
# x=lambda a:'%d is postive'%a if a>0 else('%d is negative'%a if a<0 else 'zero')
# a=int(input('enter a number'))
# print(x(a))
# Q find largest of 4 numbers
# largest=lambda a,b,c,d:"%d is largest"%a if a>b and a>c and a>d else('%d is largest'%b if b>c and b>d else('%d is largest'%c if c>d else '%d is largest'%d))
# a=int(input('enter a'))
# b=int(input('enter b'))
# c=int(input('enterc'))
# d=int(input('enter d'))
# print(largest(a,b,c,d))
#Q accept age of 4 people and display the youngest one
# youngest=lambda a,b,c,d:'%d is youngest'%a if a<b and a<c and a<d else('%d is youngest'%b if b<c and b<d else('%d is youngest'%c if c<d else '%d is youngest'%d))
# a=int(input('enter the age1'))
# b=int(input('enter the age2'))
# c=int(input('enter the age3'))
# d=int(input('enter the age4'))
# print(youngest(a,b,c,d))
# 11-05-2023
# filter()
# Q write a lambda function to filter out even numbers from the given list
# li=[2,3,4,5,6]
# x=list(filter(lambda i:i%2==0,li))
# print(x)
# x=list(filter(lambda i:i%2!=0,li))
# print(x)
# Q from the lsit filter out numbers which is devisible by 13 but not by 3 using lambda
# li=[1,213,100,220,101,33,13]
# x=list(filter(lambda i:i%13==0 and i%3!=0,li))
# print(x)
# Q filter age bw 18 and 50
# age=[12,34,28,2,50,22,1]
# x=list(filter(lambda i:i>18 and i<50,age))
# print(x)
#map()
# l=[1,2,3,4,5]
# x=list(map(lambda i:i**2,l))
# print(x)
# Q find square root of each elemnet in given list
# l=[1,4,9,16,25,36]
# x=list(map(lambda i:i**0.5,l))
# print(x)
#Q create a list from 1-10 and create multiplication values of user input
# li=[1,2,3,4,5,6,7,8,9,10]
# n=int(input('enter the number'))
# x=list(map(lambda i:i*n,li))
# print(x)
#map() using two list
# zip()
# name=['shigin','lal']
# age=[27,28]
# a=zip(name,age)
# print(list(a))
# li1=[1,2,3,4]
# li2=[5,6,7,8]
# x=list(map(lambda x,y:x+y,li1,li2))
# print(x)
# students=['shigin shigin','raju raju']
# x=list(map(lambda i:i.capitalize(),students))
# print(x)
#reduce()
from functools import reduce
# Q find largest element from the list using reduce
# li=[100,300,200,500]
# x=reduce(lambda a,b:a if a>b else b,li)
# print(x)
#Q find the smallest element from the given list
# li=[2,1,3,5,7]
# x=reduce(lambda a,b:a if a<b else b,li)
# print(x)
# Q1 find the sum of elements in list using reduce()
# li=[1,2,3,4,5,6]
# Q2 find the products of elemenets in list using reduce()
# li=[5,7,9,11,13]
# li=[1,2,3,4,5,6]
# x=reduce(lambda a,b:a+b,li)
# print('sum of the elements=%d'%x)
# li=[5,7,9,11,13]
# x=reduce(lambda a,b:a*b,li)
# print('product of element = %d'%x)
# 12-05-2023
