# class employee:
    # def __init__(self,name,salary):
        # self.name=name                          #  public data member
        # self.__salary=salary                      #private data member
    # def printval(self):                          #public function
        # print('Name=',self.name)
        # print('Salary=',self.__salary)
# obj=employee('SHIGIN',50000)
# obj.printval()                                 #will return both values bcz we can call pblic function print val
# print('name=',obj.name)
# print('salary=',obj.__salary)               #we cannot access bcz salary is private


# how to access a private data outside the class
#name mangling
# syntax
# _classname__dtatmember
class employee:
    def __init__(self,name,salary):
        self.name=name                          #  public data member
        self.__salary=salary                      #private data member
    def __printval(self):                          #public function
        print('Name=',self.name)
        print('Salary=',self.__salary)
obj=employee('SHIGIN',50000)
# obj.printval()                                 #will return both values bcz we can call pblic function print val
print('name=',obj.name)
# print('salary=',obj.__salary)
# call private data
# print('salary=',obj._employee__salary)
# call private function
# obj._employee__printval()


# protected access modifier


