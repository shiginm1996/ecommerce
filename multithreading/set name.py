# from threading import *
# import time
# def cube(a):
#     print('calculate cube')
#     for i in a:
#         print("cube=",i**3,current_thread().name)
#
# def square(a):        #thread 2
#     print('count square')
#     for i in a:
#         time.sleep(2)
#         print('square=',i**2,current_thread().name)
#
# li=[1,2,3,4]
# t1=Thread(target=cube,args=(li,))
# t1.setName("first thread")
# t2=Thread(target=square,args=(li,))
# t2.setName("second thread")
# t1.start()
# t2.start()                          #error will occure