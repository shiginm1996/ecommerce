# and

# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='employee'
# )
# mycursor=mydb.cursor()
# id=int(input('enter the id'))
# name=input('enter name')
# sql='select * from details where id=%d and name="%s"'%(id,name)
# mycursor.execute(sql)
# a=mycursor.fetchone()
# id=a[0]
# name=a[1]
# email=a[2]
# phone_number=a[3]
# print('name=',name,'email=',email,'phone number=',phone_number)

# OR
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='employee'
# )
# mycursor=mydb.cursor()
# id=int(input('enter id'))
# name=input('enter name')
# sql='select * from details where id=%d or name="%s"'%(id,name)  # priority is given on first one bcz fetch one
# mycursor.execute(sql)
# a=mycursor.fetchone()
# id=a[0]
# name=a[1]
# email=a[2]
# phone_number=a[3]
# print('name=',name,'email=',email,'phone number=',phone_number)

#iteration with fetchall    returns both the raws
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='employee'
# )
# mycursor=mydb.cursor()
# id=int(input('enter id'))
# name=input('enter name')
# sql='select * from details where id=%d or name="%s"'%(id,name)
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     id=i[0]
#     name=i[1]
#     email=i[2]
#     phone_number=i[3]
#     print('name=',name,'email=',email,'phone number=',phone_number)



# not
# sql='select * from tablename where not condition'

# # Q1. using product id
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# id=int(input('enter id'))
# sql='select * from product_details where not id=%d'%id
# mycursor.execute(sql)
# a=mycursor.fetchall()
#
# for i in a:
#     id=i[0]
#     name=i[1]
#     price=i[2]
#     cutomer_name=i[3]
#     phone_number=i[4]
#     print('id=',id,'product name=',name,'price=',price,'customer name=',cutomer_name,'phone number=',phone_number)


# Q1. using product name
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# name=input('enter name')
# sql='select * from product_details where not name="%s"'%name
# mycursor.execute(sql)
# a=mycursor.fetchall()
#
# for i in a:
#     id=i[0]
#     name=i[1]
#     price=i[2]
#     cutomer_name=i[3]
#     phone_number=i[4]
#     print('id=',id,'product name=',name,'price=',price,'customer name=',cutomer_name,'phone number=',phone_number)