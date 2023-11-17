# syntax
# class A:
#     def setv1(self):
#         print('class A')
# class B(A):
#     def setv2(self):
#         print('class B')
# class C(B):
#     def setv3(self):
#         print('class C')
# object=C()
# object.setv1()
# object.setv2()
# object.setv3()

# mobile(storage,color)
# samsung(ram)
# samsung galaxy(speed)
#
# class mobile:
#     def setv1(self,storage,color):
#         self.str=storage
#         self.cl=color
# class samsung(mobile):
#     def setv2(self,ram):
#         self.ram=ram
# class samsung_galexy(samsung):
#     def setv3(self,speed):
#         self.speed=speed
#         print('Storage=',self.str)
#         print('color=',self.cl)
#         print('ram=',self.ram)
#         print('speed=',self.speed)
# obj=samsung_galexy()
# obj.setv1('62gb','red')
# obj.setv2('8gb')
# obj.setv3('1.5ghz')

# USING CONSTRUCTOR

# car:wheel,colorsys
# maruthi:model
# maruthi 800:price

# class car:
#     def __init__(self,wheel,color):
#         self.wh=wheel
#         self.cl=color
# class maruthi(car):
#     def __init__(self,wheel,color,model):
#         car.__init__(self,wheel,color)
#         self.mod=model
# class maruthi_800(maruthi):
#     def __init__(self,wheel,color,model,price):
#         maruthi.__init__(self,wheel,color,model)
#         self.price=price
#         print('wheel=',self.wh)
#         print('color=',self.cl)
#         print('model=',self.mod)
#         print('price=',self.price)
# obj=maruthi_800('MRF','BLACK',1990,500000)










