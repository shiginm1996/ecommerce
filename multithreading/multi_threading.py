# from threading import *
# import time
# def cube(a):         #thread1
#     print('calculate cube')
#     for i in a:
#
#         print("cube=",i**3,current_thread().name)
#
# def square(a):        #thread 2
#     print('count square')
#     for i in a:
#
#         print('square=',i**2,current_thread().name)
#
# li=[1,2,3,4]
# t1=Thread(target=cube,args=(li,))           #must put comma in arg in case of single argumnet
# t2=Thread(target=square,args=(li,))
#
# t1.start()                    #for working the thread
# t2.start()
#
#
#
#
# from threading import *
# import time
# def cube(a):
#     print('calculate cube')
#     for i in a:
#         time.sleep(1)                               #put some sleep time in the function
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
# t2=Thread(target=square,args=(li,))
#
# t1.start()
# t2.start()


# to dispaly hi after complete the main thread

# from threading import *
# import time
# def cube(a):         #thread1
#     print('calculate cube')
#     for i in a:
#
#         print("cube=",i**3,current_thread().name)
#
# def square(a):        #thread 2
#     print('count square')
#     for i in a:
#
#         print('square=',i**2,current_thread().name)
#
# li=[1,2,3,4]
# t1=Thread(target=cube,args=(li,))      #change in to multithreading
# t2=Thread(target=square,args=(li,))
#
# t1.start()
# t2.start()
# t1.join()
# t2.join()
# print('hi',current_thread().name)    #will print only after main thread is end


