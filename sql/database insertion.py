# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='employee'
# )
# mycursor=mydb.cursor()
# name=input('enter name')
# email=input('enter email')
# phone_number=int(input('enter phone number'))
# sql="insert into details(name,email,phone_number)values('%s','%s','%d')"%(name,email,phone_number)
# mycursor.execute(sql)
# mydb.commit()
# print("data added successfully")


# looping
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='employee'
# )
# mycursor=mydb.cursor()
# n=int(input('enter the no of employee details'))
#
# for i in range(1,n+1):
#     name = input('enter name')
#     email = input('enter email')
#     phone_number = int(input('enter phone number'))
#     sql="insert into details(name,email,phone_number)values('%s','%s','%d')"%(name,email,phone_number)
#     mycursor.execute(sql)
#     mydb.commit()
# print("data added successfully")


# 10-06-2023
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
#
# )
# mycursor=mydb.cursor()
# n=int(input('enter the number of product'))
# for i in range(n):
#     name=input('enter the product name')
#     price=int(input('enter the price'))
#     cutomer_name=input('enter customer name')
#     phone_number=int(input('enter the phone number'))
#     sql="insert into product_details(name,price,cutomer_name,phone_number)values('%s',%d,'%s',%d)"%(name,price,cutomer_name,phone_number)
#     mycursor.execute(sql)
#     mydb.commit()
# print('data added successfully')
