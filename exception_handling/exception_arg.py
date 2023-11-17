# syntax

# try:
#     //code to be executed
# except:
    # //catch the exception

# zero division error
# a=int(input('enter a'))
# b=int(input('enter b'))
# c=a/b
# print(c)

# try:
#     a=int(input('enter a'))
#     b=int(input('enter b'))
#     c=a/b
#     print(c)
# except:
#     print("can't devided by zero")


# solve quadratic equation using exception handling

# try:
#     a=int(input('enter a'))
#     b=int(input('enter b'))
#     c= int(input('enter c'))
#     d=(b**2)-(4-a-c)**0.5
#     quad1=(-b+(d))/(2*a)
#     print(quad1)
#     quad2=(-b-d)/(2*a)
#     print(quad2)
# except:
#     print('cant devided by zero')


# value error
# try:
#     a=int(input('enter a'))
#     print(a)
# except:
#     print('please enter integer value')

# if multiple errors occures

# try:
#     a=int(input('enter a'))
#     b=int(input('enter b'))
#     c=a/b
#     print(c)
# except ZeroDivisionError:
#     print('cant devided by zero')
# except ValueError:
#     print('please enter integer value')


# name=['shigin','sharath','nandu','raku','unni']
# try:
#     position=int(input('enter the position'))
#     print(name[position])
# except IndexError:
#     print('list index out of range')
# except ValueError:
#     print('please enter integer value')

# FileNotFoundError
# import os
# try:
#     os.remove(r'C:\Users\shigi\PycharmProjects\python class\data types and methods\demo.py')
#     print('file removed')
# except:
#     print('file not found')


# import os
# try:
#     filename=input('enter the file name')
#     os.remove(fr'C:\Users\shigi\PycharmProjects\python class\data types and methods\{filename}')
#     print('file removed')                #f is used to change string to variable   r is for remove spcl charctrs
# except FileNotFoundError:
#     print('file not found')
# except ValueError:
#         print('enter string as input')

# a=int(input('enter number'))
# print(b)

# exception handling with argument


# syntax
# try:
    # //code to be executed
# except Exceptiontype as argument:
#     //exception body

# try:
#     a=int(input('enter a'))
#     b=int(input('enter b'))
#     c=a/b
#     print(c)
# except ZeroDivisionError as g:
#     print(g)

# value error
# try:
#     a=int(input('enter a'))
#     print(a)
# except ValueError as e:
#     print(e)

# index error
# str=['a','b''c']
# try:
#     pos=int(input('enter position'))
#     print(str[pos])
# except IndexError as e:
#     print(e)


# File not found
# import os
# try:
#     filename=input('enter the file name')
#     os.remove(fr'C:\Users\shigi\PycharmProjects\python class\data types and methods\{filename}')
#     print('file removed')
# except FileNotFoundError as e:
#     print(e)