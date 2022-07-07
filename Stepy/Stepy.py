# Step Control - in python
print("STEPY - STEP CONTROL IN PYTHON")
import sqlite3
conn = sqlite3.connect('Code\Stepy\Stepy.db')
cursor = conn.cursor()
print("Menu >\n1 - create table;\n2 - setup table;\n3 - print tables;")
choice=int(input("Enter your choice: "))

if(choice==1):
    conn.execute(''' CREATE TABLE step
    (DATE TEXT NOT NULL,
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
        conn.commit
        subChoice=int(input("Type 1 to exit and 0 to inserto more steps. >"))
elif(choice==3):
    print("List of steps:")
    conn.execute('SELECT * FROM step')
else:
    print("Error choice.")
conn.close

# UNDER CONSTRUTION