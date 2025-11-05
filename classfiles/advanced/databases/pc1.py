import mysql.connector


conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Apple444",
    database="pythondemo"
)
cursor = conn.cursor()
print("connection establishedcl")

# creating a table using python
create_table_query ="""
   create table employees(
   id INT AUTO_INCREMENT PRIMARY  KEY,
   name  VARCHAR(100),
   position VARCHAR(100),
   salary FLOAT
   )
    """
#cursor.execute(create_table_query)
#print("Table created")

# inserting a row 
#insert_query ="insert into employees(name,position,salary)values(%s,%s,%s)"
#values =("JN","Manager",75000)
#cursor.execute(insert_query,values)
#conn.commit() #commit transaction
#print(f"{cursor.rowcount} row inserted")

# reading data
cursor.execute(" select * from employees")
rows = cursor.fetchall()
for row in rows:
    print(row)


#update data 
    
update_query =" update employees set salary =%s where name  =%s"
cursor.execute(update_query,(8000,"JN"))
conn.commit()
print(f"{cursor.rowcount} row updated")

# delete data

#delete_query =" Delete from employees where name =%s"
#cursor.execute(delete_query,("JN",))
#conn.commit()
#print(f"{cursor.rowcount} row delete")

 #calling stored procedure
cursor.callproc('GetEmployees')
for result in cursor.stored_results():
     print(result.fetchall())

cursor.close()
conn.close()
print("connection closed")

