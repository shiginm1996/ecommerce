# class A:
#     def product(self,a,b):
#         print(a*b)
#     def product(self,a,b,c):
#         print(a*b*c)
# obj=A()
# obj.product(1,2)
# obj.product(1,2,3)

#in the above code we have defined two product method,
#but we can only use the second product method,
#as python doesnot support method overloading.
# multiple dispatch

# from multipledispatch import dispatch
# class A:
#     @dispatch(int,int)
#     def product(self,a,b):
#         print(a*b)
#     @dispatch(int,int,int)
#     def product(self,a,b,c):
#         print(a*b*c)
# obj=A()
# obj.product(1,2)
# obj.product(1,2,3)
# from multipledispatch import dispatch
# class A:
#     @dispatch(str,str)
#     def add_string(self,a,b):
#         print(a+b)
#     @dispatch(str,str,str)
#     def add_string(self,a,b,c):
#         print(a+b+c)
# obj=A()
# obj.add_string('shi','gin')
# obj.add_string('shig','in','madappally')

# from multipledispatch import dispatch
# class A:
#     @dispatch(float,float)
#     def add(self,a,b):
#         print(a*b)
#     @dispatch(float,float,float)
#     def add(self,a,b,c):
#         print(a+b+c)
# obj=A()
# obj.add(1.1,2.5)
# obj.add(1.6,2.8,3.4)