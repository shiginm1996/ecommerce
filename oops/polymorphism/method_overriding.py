# class father:
#     def phone(self):
#         print('fathers phone')
# class child(father):
#     def phone(self):
#         pass
# obj=child()
# obj.phone()

# class father:              #  here childs body override father body.
#     def phone(self):
#         print('fathers phone')
# class child(father):
#     def phone(self):
#         print("child's phone")
# obj=child()
# obj.phone()


# overriding with multiple inheritance
# syntax
# class A:
#     def fun(self):
#         print('class A')
# class B:
#     def fun1(self):
#         print('class B')
# class C(A,B):
#     def fun(self):
#         print('class A changes to class C')
#     def fun1(self):
#         print('class B changes to class c')                #class C overrides class A and Class B
# obj=C()
# obj.fun()
# obj.fun1()

# overriding using ,multilevel inheretance
# class A:
#     def fun(self):
#         print('class A')
# class B(A):
#     def fun(self):
#         print('class A changed to class B')
# class C(B):
#     def fun(self):
#         print('class B changed to class c')
#
# obj=C()
# obj.fun()

# method overriding using hierarchical inheritance
# class A:
#     def fun(self):
#         print('class A')
# class B(A):
#     def fun(self):
#         print('class A replaces class B')
# class C(A):
#     def fun(self):
#         print('class A replaces class C')
# obj=B()
# obj.fun()
# obj1=C()
# obj1.fun()

# method overriding using hybrid inheritance
# class A:
#     def fun(self):
#         print('class A')
# class B(A):
#     def fun(self):
#         print('class B')          #class B replaces A
# class C(A):
#     def fun(self):
#         print('class C')         #CLASS c replaces A
# class D(B,C):
#     def fun(self):
#         print('class C')           #class C replaces A,B,C
# obj=C()
# obj.fun()
# obj=B()
# obj.fun()
# obj=C()
# obj.fun()
