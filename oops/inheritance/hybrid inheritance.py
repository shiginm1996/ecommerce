# syntax
# class parent:
#     def fun(self):
#         print('parent class')
# class A(parent):
#     def fun1(self):
#         print('child A')
# class B(parent):
#     def fun2(self):
#         print('child B')
# class C(A,B):
#     def fun3(self):
#         print('child C')
# obj1=C()
# obj1.fun()
# obj1.fun1()
# obj1.fun2()
# obj1.fun3()

# university  parent(univ_name,location)
# college   childA   (college name)
# course     childB   (course_name)
# student    childC    (roll no,name)

# class university:
#     def fun(self,univ_name,location):
#         self.univnm=univ_name
#         self.loc=location
#         print('University name=',self.univnm)
#         print('Location=',self.loc)
# class college(university):
#     def fun1(self,college_name):
#         self.clgnm=college_name
#         print('College Name=',self.clgnm)
# class course(university):
#     def fun2(self,course_name):
#         self.coursenm=course_name
#         print('Course Name=',self.coursenm)
# class student(college,course):
#     def fun3(self,roll_n,name):
#         self.rollno=roll_n
#         self.name=name
#         print('Roll Name=',self.rollno)
#         print('Name=',self.name)
# obj=student()
# obj.fun('Kannur University','Kannur')
# obj.fun1('CAS COLLEGE MADAYI')
# obj.fun2('Mcom')
# obj.fun3(8,'SHIGIN M')
#
#
# WORK: using constructor
# university  parent(univ_name,location)
# college   childA   (college name)
# course     childB   (course_name)
# student    childC    (roll no,name)
#
class university:
    def __init__(self,univ_name,location):
        self.unvnm=univ_name
        self.loc=location

class college(university):
    def __init__(self,univ_name,location,college_name):
        university.__init__(self,univ_name,location)
        self.clgnm=college_name

class course(university):
    def __init__(self,univ_name,location,course_name):
        university.__init__(self,univ_name,location)
        self.coursnm=course_name

class student(college,course):
    def __init__(self,univ_name,location,college_name,course_name,roll_no,name):
        college.__init__(self,univ_name,location,college_name)
        course.__init__(self,univ_name,location,course_name)
        self.rolno=roll_no
        self.name=name
        print('University Name=', self.unvnm)
        print('Location=', self.loc)
        print('College Name=', self.clgnm)
        print('Course Name=', self.coursnm)
        print('Roll No.=',self.rolno)
        print('Name=',self.name)
obj=student('KANNUR UNIVERSITY','KANNUR','CAS COLLEGE MADAYI','MCOM',8,'SHIGIN M')





