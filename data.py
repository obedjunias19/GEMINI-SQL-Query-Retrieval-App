import sqlite3

# Connect to SQLiteDB
connection=sqlite3.connect("student.db")

# Create a cursor object to create table and insert record

cursor=connection.cursor()

# create the table
table_info="""
Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
SECTION VARCHAR(25),MARKS INT);

"""
cursor.execute(table_info)

## Insert records

cursor.execute('''Insert Into STUDENT values('Obed Junias','Machine Learning','A',100)''')
cursor.execute('''Insert Into STUDENT values('Ajay','Machine Learning','B',77)''')
cursor.execute('''Insert Into STUDENT values('Dwayne','Machine Learning','A',94)''')
cursor.execute('''Insert Into STUDENT values('Taylor Swift','Algorithms','B',74)''')
cursor.execute('''Insert Into STUDENT values('John Doe','Algorithms','C',64)''')
cursor.execute('''Insert Into STUDENT values('Emma Watson','Data Science','A',92)''')
cursor.execute('''Insert Into STUDENT values('Samuel Jackson','Data Science','B',86)''')
cursor.execute('''Insert Into STUDENT values('Olivia Johnson','Data Science','A',98)''')
cursor.execute('''Insert Into STUDENT values('Michael Jordan','Artificial Intelligence','C',68)''')
cursor.execute('''Insert Into STUDENT values('Megan Anderson','Artificial Intelligence','C',60)''')
cursor.execute('''Insert Into STUDENT values('Sophia Miller','Machine Learning','A',95)''')
cursor.execute('''Insert Into STUDENT values('Ethan Brown','Machine Learning','B',82)''')
cursor.execute('''Insert Into STUDENT values('Ava Davis','Algorithms','A',88)''')
cursor.execute('''Insert Into STUDENT values('Logan Patel','Algorithms','C',60)''')
cursor.execute('''Insert Into STUDENT values('Isabella Lee','Data Science','A',96)''')
cursor.execute('''Insert Into STUDENT values('Liam Chen','Data Science','B',87)''')
cursor.execute('''Insert Into STUDENT values('Harper Kim','Artificial Intelligence','C',65)''')
cursor.execute('''Insert Into STUDENT values('Noah Gupta','Artificial Intelligence','B',78)''')



## Display the DB records

print("The records of the database are as follows: \n")
data=cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

## Commit the changes to database
connection.commit()
connection.close()