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
# sql='update details set name="%s" where id=%d'%(name,id)
# mycursor.execute(sql)
# mydb.commit()                        #commit bcz in to the database...not getting something from database
# print('database updated....')



# multiple updation


# Q. update customer name and phone number using id

# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# id=int(input('enter id'))
# customer_name=input('enter name')
# phone_number=int(input('enter number'))
# sql='update product_details set cutomer_name="%s",phone_number=%d where id=%d'%(customer_name,phone_number,id)
# mycursor.execute(sql)
# mydb.commit()
# print('updated successfully')



# with two condition

# update product price using id and product name
# import pymysql
# mydb=pymysql.connect(
#     host='localhost',
#     user='root',
#     password='',
#     database='product'
# )
# mycursor=mydb.cursor()
# id=int(input('enter id'))
# name=input('enter name')
# price=int(input('enter price'))
# sql='update product_details set price=%d where id=%d and name="%s"'%(price,id,name)
# mycursor.execute(sql)
# mydb.commit()
# print('updated successfully')