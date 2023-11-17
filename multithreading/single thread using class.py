# from threading import *
# import time
# class hello:  #thread class
#     def run(self):               #default=run
#         for i in range(5):
#             time.sleep(2)
#             print("hello",current_thread().name)
# class hai:
#     def run(self):
#         for i in range(5):
#             print("hi....",current_thread().name)
# t1=hello()
# t2=hai()
# t1.run()
# t2.run()

# converting in to multithreading class
# from threading import *
# import time
# class hello(Thread):  #thread class
#     def run(self):               #default=run
#         for i in range(5):
#             # time.sleep(2)
#             print("hello",current_thread().name)
# class hai(Thread):
#     def run(self):
#         for i in range(5):
#             print("hi....",current_thread().name)
# t1=hello()
# t2=hai()
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print("this is a thread",current_thread().name)



# from threading import *
# import time
# class hello(Thread):
#     def add(self,a,b):
#         print(a+b,current_thread().name)
# class hai(Thread):
#     def sub(self,a,b):
#         print(a-b,current_thread().name)
#
# t1=hello()
# t2=hai()
# t1.add(1,2)
# t2.sub(5,3)
# print("this is a thread",current_thread().name)

#* it is working as single thread.so result will be main thread.



# usoing constructor

# from threading import *
# class hello(Thread):
#     def __init__(self,a,b):
#         Thread.__init__(self)
#         self.a=a
#         self.b=b
#     def run(self):
#         print(self.a+self.b,current_thread().name)
# t1=hello(1,2)
# t1.start()


# create a class multiply,pass three argument,print the product 3 times
# from threading import *
# import time
# class multiply(Thread):
#     def __init__(self,a,b,c):
#         Thread. __init__(self)
#         self.a=a
#         self.b=b
#         self.c=c
#     def run(self):
#             for i in range(3):
#
#                 print(self.a*self.b*self.c,current_thread().name)
#
# t1=multiply(1,2,3)
# t1.start()
# t1.join()
# print('hello gyzzz.......')





