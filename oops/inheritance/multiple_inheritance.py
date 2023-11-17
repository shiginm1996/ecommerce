# syntax
# class A:
#     def fun1(self):
#         print('class A')
# class B:
#     def fun2(self):
#         print('class B')
# class C(A,B):
#     def fun3(self):
#         print('class C')
# obj=C()
# obj.fun1()
# obj.fun2()
# obj.fun3()


# parent=father(fname,address),mother(mname)
# child=son(sname)
# create 2 son object

# class father:
#     def setv1(self,fname,address):
#         self.fname=fname
#         self.ad=address
#         print('father name=',self.fname)
#         print('address=',self.ad)
# class mother:
#     def setv2(self,mname):
#         self.mnm=mname
#         print('mother name=',self.mnm)
# class son(father,mother):
#     def setv3(self,sname):
#         self.snm=sname
#         print('son name=',self.snm)
# obj=son()
# obj.setv1('sureshan','kochi')
# obj.setv2('shantha')
# obj.setv3('arun')
# print()
# obj1=son()
# obj1.setv1('babu','kannur')
# obj1.setv2('vanaja')
# obj1.setv3('tintu')

# using constructor

# class father:
#     def __init__(self,fname):
#         self.fname=fname
# class mother:
#     def __init__(self,mname):
#         self.mname=mname
# class son(father,mother):
#     def __init__(self,fname,mname,sname):
#         father.__init__(self,fname)
#         mother.__init__(self,mname)
#         self.sname=sname
#         print('father name=',self.fname)
#         print('mother name=',self.mname)
#         print('son name=',self.sname)
# obj=son('raju','rajasree','gopu')
# print()
# obj1=son('raju','rajasree','ammu')

# parent:company(name and location)
# parent2:team leader(name,department)
# worker(emp_name,designation and salary)

# class company:
#     def __init__(self,comp_name,location):
#         self.compnm=comp_name
#         self.loc=location
# class team_leader:
#     def __init__(self,TLname,department):
#         self.tlnm=TLname
#         self.dprt=department
# class worker(company,team_leader):
#     def __init__(self,comp_name,location,TLname,department,emp_name,designation,salary):
#         company.__init__(self,comp_name,location)
#         team_leader.__init__(self,TLname,department)
#         self.empnm=emp_name
#         self.des=designation
#         self.sal=salary
#         print('comapny name=',self.compnm)
#         print('location=',self.loc)
#         print('TL name=',self.tlnm)
#         print('Department=',self.dprt)
#         print('employee name=',self.empnm)
#         print('designation=',self.des)
#         print('salary=',self.sal)
# obj=worker('TCS','KOCHI','SHIGIN','IT','SANAL','JUNIOR DEVELOPER',45000)
# print()
# obj1=worker('TCS','KOCHI','SHIGIN','IT','KARTHIK','JUNIOR DEVELOPER',40000)




