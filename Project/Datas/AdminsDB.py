import os
import sqlite3 as sql


# Switching Working Directory
# ----------------------------------
if os.getcwd().endswith("\Datas\Database"):
    pass
else:
    os.chdir("Project/Datas/Database")
# ---------------------------------

# Admins Database Module
# --------------------------------------------------

conn = sql.connect('database.db')
cur = conn.cursor()

def admin_new(f_name: str, l_name: str, username: str, password: str, national_code: str, birthdate: str, gender: str):
    admin = (f_name, l_name, username, password, national_code,
             birthdate, gender)
    cur.execute("INSERT INTO admins VALUES(?,?,?,?,?,?,?)",admin)
    conn.commit()

def admin_datas():
    cur.execute("SELECT * FROM admins")
    admins = cur.fetchall()
    for admin in admins:
        print(admin)
# ---------------------------------------------------