# 31. Write a Python program to calculate the area of a circle

# r=int(input('enter the radius'))
# area=3.14*(r**2)
# print('area of circle=',area)


# 32. Create a program that checks if a given number is a perfect square.

# n=int(input('enter a number'))
# a=n**0.5
# if n%a==0:
#     print('square')
# else:
#     print('not square')


# 33. Write a program to find the square root of a number.

# n=int(input('enter a number'))
# sq=n**0.5
# print('square root of %d = %f'%(n,sq))

# 34. Create a program that generates a simple to-do list.

# li=[]
# while True:
#     print('choice','\n1.add','\n2.display','\n3.remove')
#     choice=int(input('enter the choice'))
#     if choice==1:
#         l=int(input('enter the limit'))
#         for i in range(0,l):
#             el=input('enter element')
#             li.append(el)
#         print('added successfully')
#     elif choice==2:
#         print(li)
#     elif choice==3:
#         li.pop()
#         print('item removed')
#     else:
#         print('choose correct')
#         break


# 35. Write a Python program to find the LCM (Least Common Multiple) of two numbers.







# 36. Create a program to check if a string contains only alphabetic characters

# a=input('enter something')
# if a.isalpha():
#     print('yes')
# else:
#     print('no')

# 37. Write a program that calculates the power of a number (a^b).
# a=int(input('enter number'))
# b=int(input('power'))
# print('%d^%d=%d'%(a,b,(a**b)))


# 38. Create a program to calculate the sum of all natural numbers up to a given N.
# s=0
# n=int(input('enter the number'))
# for i in range(0,n):
#     s+=i
# print('sum of %d natural numbers=%d'%(n,s))

# 39. Write a Python program to find the factorial of a number using a loop
# f=1
# n=int(input('enter the number'))
# for i in range(1,n+1):
#     f*=i
# print('factorial of %d=%d'%(n,f))



# 40. Create a program to check if a string is a valid email address.

# email=input('enter email')
# a=email.split('.')
# if '@' in a[0] and 'com' in a[1] and '.' in email and 'gmail' in a[0]:
#     print('valid')
# else:
#     print('invalid')


# 41. Write a program to reverse a list in Python

# li=[1,5,8,9,2,7]
# rev=[]
# leng=len(li)
# print(leng)
# for i in range(len(li)-1,-1,-1):
#     rev.append(li[i])
# print(rev)







