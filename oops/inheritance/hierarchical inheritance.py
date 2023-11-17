# syntax
# class A:
#     def fun(self):
#         print('class A')
# class B(A):
#     def fun1(self):
#         print('class B')
# class C(A):
#     def fun2(self):
#         print('class C')
# class D(A):
#     def fun3(self):
#         print('class D')
# obj=B()
# obj.fun()
# obj.fun1()
# print()
# obj1=C()
# obj1.fun()
# obj1.fun2()
# print()
# obj2=D()
# obj2.fun()
# obj2.fun3()

# details:id,name,gender  parent
# developer: designation,company name    child class 1
# doctor: hospital,specialization   child2

# class details:
#     def fun1(self,id,name,gender):
#         self.id=id
#         self.name=name
#         self.gender=gender
#         print('id=',self.id)
#         print('name=',self.name)
#         print('gender=',self.gender)
# class developer(details):
#     def fun2(self,designation,comp_name):
#         self.des=designation
#         self.comp=comp_name
#         print('designation=',self.des)
#         print('compnay name=',self.comp)
# class doctor(details):
#     def fun3(self,hospital,specialization):
#         self.hos=hospital
#         self.spc=specialization
#         print('hospital=',self.hos)
#         print('specialization=',self.spc)
# obj=developer()
# obj.fun1(121,'abc','male')
# obj.fun2('hr','hrms solution')
# print()
#
# obj1=doctor()
# obj1.fun1(121,'abc','male')
# obj1.fun3('hml hospital','MD')

# same using constructor
# details:id,name,gender  parent
# developer: designation,company name    child class 1
# doctor: hospital,specialization   child2

class details:
    def __init__(self,id,name,gender):
        self.id=id
        self.name=name
        self.gender=gender
        print('id=',self.id)
        print('name=',self.name)
        print('gender=',self.gender)
class developer(details):
    def __init__(self,id,name,gender,designation,company_name):
        details.__init__(self,id,name,gender)
        self.designation=designation
        self.company_name=company_name
        print('designation=',self.designation)
        print('company name=',self.company_name)
class hospital(details):
    def __init__(self,id,name,gender,hospital,specialization):
        details.__init__(self,id,name,gender)
        self.hospital = hospital
        self.spec = specialization
        print('hospital=', self.hospital)
        print('specialiazation=', self.spec)
obj=developer(9116,'SHIGIN','MALE','SOFTWARE DEVELOPER','TCS')
print()
obj1=hospital(9116,'SHIGIN','MALE','LOURDE HOSPITAL','ORTHO')







