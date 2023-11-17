# import pymysql
# # pip install  pymysql   in terminal
# # settings package pymysql
#
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password=''
# )
#
# # create a cursor object
# # used to get data from database
# mycursor=mydb.cursor()
#
# # create database   same database name duplication is not possible   #case sensitive upper or lower
#
# sql='create database employee'
# mycursor.execute(sql)
# print('database created successfully')
#
#
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password=''
# )
# mycursor=mydb.cursor()
# sql='create database employee'
# mycursor.execute(sql)
# print('database created successfully')

# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password=''
# )
# mycursor=mydb.cursor()
# newdb='create database student'
# mycursor.execute(newdb)
# print('database created successfully')

# table creation

# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='employee'
# )
# mycursor=mydb.cursor()
# sql='create table details(id int auto_increment,name varchar(50),email varchar(50),phone_number bigint(10),primary key(id))'
# mycursor.execute(sql)
# mydb.commit()
# print('table created successfully')

# create a table in product details details in product database student
# # id, name, price customer name,phone number
#
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password=''
# )
# mycursor=mydb.cursor()
# nwdb='create database product'
# mycursor.execute(nwdb)
# print('database created successfully')

import pymysql
mydb=pymysql.connect(
    host='localhost',
    user='root',
    password='',
    database='product'

)
mycursor=mydb.cursor()
sql='create table product_details(id int auto_increment,name varchar(50),price int,cutomer_name varchar(50),phone_number bigint(10),primary key(id))'
mycursor.execute(sql)
mydb.commit()
print('table created successfully')