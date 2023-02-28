import os
import sqlite3 as sql

# Person Database Module
# Creating DB File
# --------------------------------------------------
# Switching Working Directory
# ----------------------------------
if os.getcwd().endswith("\Datas\Database"):
    pass
else:
    os.chdir("Project/Datas/Database")
# ---------------------------------
conn = sql.connect("database.db")
cur = conn.cursor()

# --------------------------------------------------

def customer_new(f_name: str, l_name: str, national_code: str, birthdate: str, gender: str, overall_budget: str):
    person = [f_name, l_name, national_code,
              birthdate, gender, overall_budget]
    cur.execute("INSERT INTO customers VALUES(?,?,?,?,?,?)",person)
    conn.commit()


def customer_datas():
    cur.execute("SELECT * FROM customers")
    persons = cur.fetchall()
    for person in persons:
        print(person)

# ---------------------------------------------------