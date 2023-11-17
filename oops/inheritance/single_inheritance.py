# syntax
# class A:   #parent
#     def setval(self):
#         print("i'm parent")
# class B(A):   #child
#     def setval1(self):
# #         print("i'm child")
# # obj=B()
# # obj.setval()
# # obj.setval1()
#
# # company:parnet class,dynamic:cpmany name and location)
# # employee:child class,dynamic:name,id,salary,phone
#
# class company:
#     def setval(self,comp_name,location):
#         self.comp=comp_name
#         self.loc=location
#         print('company name=',self.comp)
#         print('location=',self.loc)
# class employee(company):
#     def setval1(self,emp_name,id,salary,phone):
#         self.empnm=emp_name
#         self.id=id
#         self.salary=salary
#         self.phone=phone
#         print('employee name=',self.empnm)
#         print('employee id=',self.id)
#         print('salary=',self.salary)
#         print('phone number=',self.phone)
# obj=employee()
# obj.setval('abc','kakkanad')
# print()
# obj.setval1('shigin',121,65000,5465466)

# single inheritance using constructor
# syntax
# class A:
#     def __init__(self):
#         print('parent class')
# class B(A):
#     def setval(self):
#         print('child class')
#         super().__init__()            #used to call constructor of parent
# obj=B()
# obj.setval()


# class vehicle:
#     def __init__(self,name,number):
#         self.name=name
#         self.number=number
#         print('vehicle name=',self.name)
#         print('vehicle number=',self.number)
# class car(vehicle):
#     def __init__(self,name,number,color,price):
#         super().__init__(name,number)
#         self.color=color
#         self.price=price
#         print('color=',self.color)
#         print('price=',self.price)
# obj=car('a',1,'red',2000000)

# implement a single inheritance using constructor and static variable

# class shape:
#     def __init__(self,color):
#         self.cl=color
#         print('color=',self.cl)
# class circle(shape):
#     def __init__(self,width,height):
#         self.width=width
#         self.height=height
#         print('width=',self.width)












