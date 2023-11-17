# class ZeroError(Exception):
#     pass
# class NegativeError(Exception):
#     pass
# try:
#     num=int(input('enter a number'))
#     if num==0:
#         raise ZeroError
#     elif num<0:
#         raise NegativeError
#     else:
#         print('success,it is a positive number ')
# except ZeroError:
#     print('Zero error occured')
# except NegativeError:
#     print('Negative Error Occured')


#
# age>50     TooOldException
# age<21     TooYoungException
# else        you are registered
# class TooOld(Exception):
#     pass
# class TooYoung(Exception):
#     pass
# try: 
#     age=int(input('enter age'))
#     if age>50:
#         raise TooOld
#     elif age<21:
#         raise TooYoung
#     else:
#         print('You are Registered')
# except TooOld:
#     print('please enter the age below 50')
# except TooYoung:
#     print('please enter the age above 21')