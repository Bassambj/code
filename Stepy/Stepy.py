# Step Control - in python
print("STEPY - STEP CONTROL IN PYTHON")
import sqlite3

conn = sqlite3.connect('Stepy.db')

# VERIFICAR SE A TABELA EXISTE SE NAO EXISTIR:
table = conn.execute(
    """SELECT step FROM Stepy.db
""").fetchall

# SE A TABELA NÃAO EXISTIR ELA É CRIADA
if table == []:
    conn.execute(''' CREATE TABLE step
        (ID INT PRIMARY KEY NOT NULL,
        DATE TEXT NOT NULL,
        QUANTY INT NOT NULL,
        ANNOTATION TEXT);''')

# UNDER CONSTRUTION