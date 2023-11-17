# class class_name:                 #no brackets while defining
#     def function_name(self):
#         print('hello')
# obj=class_name()                  #need brackets while calling
# obj.function_name()
# add 2 numbers
# class add:
#     def sum(self,a,b):
#         print(a+b)
# c=add()
# c.sum(1,2)

# object
# class laptop:
#     def setval(self,name,os,ram,price):      #self:self variable of member function
#         self.name=name
#         self.os=os
#         self.ram=ram
#         self.price=price
#         print('laptop name=',self.name)
#         print('os=',self.os)
#         print('ram=',self.ram)
#         print('price=',self.price)
# obj=laptop()
# obj.setval('hp','windows','8gb',52000)
# obj1=laptop()
# obj.setval('dell','windows','8gb',30000)

# Q create a class person with arguments
# pers name,age,gender,height,weight
# creat 3 person object

# class pers:
#     def p(self,name,age,gender,height,weight):
#         self.nm=name
#         self.ag=age
#         self.gen=gender
#         self.hei=height
#         self.wei=weight
#         print('name=',self.nm)
#         print('age=',self.ag)
#         print('gender=',self.gen)
#         print('height=',self.hei)
#         print('weight=',self.wei)
# object=pers()
# object.p('shigin',27,'male',171,63)     here repalcing of shigin to drishya in object
# object.p('drishya',25,'female',168,55)   so we are creating seperate reference variable
# object.p('unni',29,'male',172,75)

# or
# object=pers()
# object.p('shigin',27,'male',171,63)    #reference variable name is changed to find seperate products
# object1=pers()
# object1.p('drishya',25,'female',168,55)
# object2=pers()
# object.p('unni',29,'male',172,75)


