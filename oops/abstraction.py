# from abc import ABC,abstractmethod         #abc=packages   ABC=module
# class vehicle(ABC):          #abstract class and will inherit ABC
#     @abstractmethod
#     def wheel(self):
#         pass
#     @abstractmethod
#     def door(self):
#         pass
# class car(vehicle):
#     def wheel(self):
#         print('four wheels')
#     def airbag(self):                 #we can use additional function argument
#         print('have airbag')
#     def door(self):
#         print('four doors')
# obj=car()
# obj.wheel()
# obj.airbag()
# obj.door()

# class:animal
#
# from abc import ABC,abstractmethod
# # class animal(ABC):
#       @abstractmethod
# #     def sound(self):
# #         pass
#       @abstractmethod
#     def eye(self):
#         pass
# class lion(animal):
#     def sound(self):
#         print('grrr')
#     def eye(self):
#         print('2 eyes')
#     def leg(self):
#         print('four legs')
# class snake(animal):
#     def sound(self):
#         print('zzzz')
#     def poison(self):
#         print('it is poisonous')
#     def eye(self):
#         print('2 eyes')
# obj=lion()
# obj.sound()
# obj.eye()
# obj.leg()
# obj1=snake()
# obj1.sound()
# obj1.poison()
# obj1.eye()

# from abc import ABC,abstractmethod
# class A(ABC):
#     @abstractmethod
#     def __init__(self,name,address):
#         pass
#     @abstractmethod
#     def hello(self):                #we cannot use to multiple init ina single class in case of abstract method
#         pass
# class B(A):
#     def __init__(self,name,address):
#         super().__init__(name,address)
#         self.name=name
#         self.address=address
#         print('Name=',self.name)
#         print('Address=',self.address)
#     def hello(self):
#         print('hello world')
# obj=B('SHIGIN','KANNUR')
# obj.hello()



# 1.C
# 2.C
# 3.c
# 4.b
# 5.b
# 6.c
# 9.d
# 10.D
# 8.A
# 7.A










