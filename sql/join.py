# create a new table with filed id,name,color
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# sql='create table new_product_details(id int auto_increment,product_name varchar(50),color varchar(50),primary key(id))'
# mycursor.execute(sql)
# mydb.commit()
# print('table created successfully')

# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# n=int(input('enter the no of products'))
# #
# # for i in range(1,n+1):
# #     product_name = input('enter name')
# #     color = input('enter color')
# #     sql="insert into new_product_details(product_name,color)values('%s','%s')"%(product_name,color)
# #     mycursor.execute(sql)
# #     mydb.commit()
# # print("data added successfully")
#
# #syntax: sql='select table_name1.column_name1,table_name2.column_name2,table_name2.columnname1,table_name2.column_name2 from table_name1 inner join table_name2 on table_name1.id=table_name2.id'
#
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# sql='select product_details.name,product_details.price,new_product_details.product_name,new_product_details.color from product_details inner join new_product_details on product_details.id=new_product_details.id'
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     name=i[0]
#     price=i[1]
#     color=i[3]
#     print('name=',name,'price=',price,'color',color)


# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# sql="select poduct_details.name,product_details.price,product_details.cutomer_name,new_product_details.color from product_details inner join new_product_details on product_details.name=new_product_details.product_name"
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     name=i[0]
#     price=i[1]
#     cutomer_name=i[2]
#     color=i[3]
#     print('product name=',name)
#     print('price=',price)
#     print('customer name=',cutomer_name)
#     print('color=',color)
#     print()




#Q. create a table student with fileds stuent name,roll number,school name(id default)
#create another table marklist  with fileds id(default),roll number, maths,chemistry,english
#add three data
#inner join student and mark list using roll number  return:student name,maths,chemistry english

# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='student'
# )
# mycursor=mydb.cursor()
# sql='create table student_details(id int auto_increment,student_name varchar(50),roll_number int,school varchar(50),primary key(id))'
# mycursor.execute(sql)
# mydb.commit()
# print('table created successfully')

# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='student'
# )
# mycursor=mydb.cursor()
# n=int(input('enter the no of students'))
# for i in range(n):
#     student_name=input('enter the name')
#     roll_number=int(input('enter the roll number'))
#     school=input('enter the school name')
#     sql="insert into student_details(student_name,roll_number,school)values('%s',%d,'%s')"%(student_name,roll_number,school)
#     mycursor.execute(sql)
#     mydb.commit()
# print("data added successfully")


# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='student'
# )
# mycursor=mydb.cursor()
# sql='create table marklist(id int auto_increment,roll_number int,maths int,chemistry int,english int,primary key(id))'
# mycursor.execute(sql)
# mydb.commit()
# print('table created successfully')


# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='student'
# )
# mycursor=mydb.cursor()
# n=int(input('enter the no of students'))
# for i in range(n):
#     roll_number=int(input('enter the roll number'))
#     maths=int(input('enter the maths mark'))
#     chemistry=int(input('enter the chemistry mark'))
#     english=int(input('enter the english mark'))
#     sql="insert into marklist(roll_number,maths,chemistry,english)values(%d,%d,%d,%d)"%(roll_number,maths,chemistry,english)
#     mycursor.execute(sql)
#     mydb.commit()
# print("data added successfully")

# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='student'
# )
# mycursor=mydb.cursor()
# sql="select student_details.student_name,marklist.maths,marklist.chemistry,marklist.english from student_details inner join marklist on student_details.roll_number=marklist.roll_number"
# mycursor.execute(sql)
# a=mycursor.fetchall()
# print('maths','\t\tchemistry','\t\tenglish','\t\tname')
# for i in a:
#     student_name=i[0]
#     maths=i[1]
#     chemistry=i[2]
#     english=i[3]
#     print(' ',maths,'\t\t  ',chemistry,'\t\t\t  ',english,'\t\t\t ',student_name)


# Q1. add new column and update the values in column
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='student'
# )
# mycursor=mydb.cursor()
# sql='alter table student_details add location varchar(200)'
# mycursor.execute(sql)
# mydb.commit()
# print('column added successfully')

# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='student'
# )
# mycursor=mydb.cursor()
# id=int(input('enter id'))
# location=input('enter location')
# sql='update student_details set location="%s" where id=%d'%(location,id)
# mycursor.execute(sql)
# mydb.commit()                        #commit bcz in to the database...not getting something from database
# print('database updated....')


# Q. add new column and automatically fill the column

# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='student'
# )
# mycursor=mydb.cursor()
# sql='alter table marklist add total int as (maths+chemistry+english)'
# mycursor.execute(sql)
# mydb.commit()
# print('column added successfully')
#


#Q1. remove a column
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='student'
# )
# mycursor=mydb.cursor()
# sql='alter table student_details drop location'
# mycursor.execute(sql)
# mydb.commit()
# print('column removed successfully')



# 19-06-2023
# for deleting a table
# sql="drop table table_name"

# truncate
# sql="truncate table table_name"

# delete database
# sql="drop database database_name"


# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password=''
# )
# mycursor=mydb.cursor()
# sql='create database staff'
# mycursor.execute(sql)
# print('database created successfully')

# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='staff'
# )
# mycursor=mydb.cursor()
# sql='create table staff_details(id int auto_increment,name varchar(50),primary key(id))'
# mycursor.execute(sql)
# mydb.commit()
# print('table created successfully')



# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='staff'
# )
# mycursor=mydb.cursor()
# n=int(input('enter the no of staff'))
#
# for i in range(n):
#     name = input('enter name')
#     sql="insert into staff_details(name)values('%s')"%(name)
#     mycursor.execute(sql)
#     mydb.commit()
# print("data added successfully")


# truncate table staff_details
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='staff'
# )
# mycursor=mydb.cursor()
# sql="truncate table staff_details"
# mycursor.execute(sql)
# mydb.commit()
# print('truncated completed')


#delete table staff_details
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='staff'
# )
# mycursor=mydb.cursor()
# sql="drop table staff_details"
# mycursor.execute(sql)
# mydb.commit()
# print('table deleted')


#delete database staff
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='staff'
# )
# mycursor=mydb.cursor()
# sql="drop database staff"
# mycursor.execute(sql)
# mydb.commit()
# print('database deleted')





