# Step Control - in python
# sqlite3 - basic commands in python.
# Reference: https://docs.python.org/pt-br/3/library/sqlite3.html?highlight

print("STEPY - STEP CONTROL IN PYTHON")
import sqlite3
conn = sqlite3.connect('Code\Stepy\Stepy.db')
cursor = conn.cursor()
print("Menu >\n1 - Create table;\n2 - Record data;\n3 - Print rows; \n4 - Delete row;")
choice=int(input("Enter your choice: "))

if(choice==1):
    conn.execute(''' CREATE TABLE step
    (ID INT NOT NULL,
    DATE TEXT NOT NULL,
    QUANTY INT NOT NULL,
    ANNOTATION TEXT);''')
elif(choice==2):
    subChoice=0
    while(subChoice!=1):
        print("Insert step...")
        date=input("Enter the date: ")
        quanty=int(input("Enter the quant.: "))
        annot=input("Enter any annotation: ")
        cursor.execute(""" INSERT INTO step (DATE, QUANTY, ANNOTATION) VALUES (?,?,?) """, (date,quanty,annot))
        conn.commit()
        subChoice=int(input("Type 1 to exit and 0 to inserto more steps. >"))
elif(choice==3):
    print("List of steps:")
    for row in conn.execute('SELECT * FROM step'):
        print(row)
elif(choice==4):
    print("DELETE ROW")
    print("Enter the ID number that will ve DELETED: ")
    idRow=
    
else:
    print("Error choice.")
conn.close