# default=ascending
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='employee'
# )
# mycursor=mydb.cursor()
# sql="select * from details order by name"
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     id=i[0]
#     name=i[1]
#     email=i[2]
#     phone_number=i[3]
#     print('id=',id,'\tname=',name,'\temail',email,'\tphone number=',phone_number)

#
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# sql="select * from product_details order by price"
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     id=i[0]
#     name=i[1]
#     price=i[2]
#     cutomer_name=i[3]
#     phone_number=i[4]
#     print('id=',id)
#     print('product name=',name)
#     print('price=',price)
#     print('customer name=',cutomer_name)
#     print('phone number=',phone_number)
#     print()


# Q. select product name and price from product table order the product by price
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# sql="select name,price from product_details order by price"
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     name=i[0]
#     price=i[1]
#     print('product name=',name)
#     print('price=',price)
#     print()


# Sort by descending order

# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# sql="select * from product_details order by price desc"
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     id=i[0]
#     name=i[1]
#     price=i[2]
#     cutomer_name=i[3]
#     phone_number=i[4]
#     print('id=',id)
#     print('product name=',name)
#     print('price=',price)
#     print('customer name=',cutomer_name)
#     print('phone number=',phone_number)
#     print()



#it is possible to order one column as ascending and nother as descending
# sql="select name,cutomer_name from table_name order by name asc cutomer_name desc"

import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# sql="select name,cutomer_name from product_details order by name asc,cutomer_name desc"
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     name=i[0]
#     cutomer_name=i[1]
#     print('product name=',name)
#     print('customer name=',cutomer_name)
#     print()



# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# sql="select name,price from product_details order by name asc,price desc"
# mycursor.execute(sql)
# a=mycursor.fetchall()
# for i in a:
#     name=i[0]
#     price=i[1]
#     print('product name=',name,'\t\tprice=',price)





