import sqlite3 as sql
import os

# Switching Working Directory
# ----------------------------------
if os.getcwd().endswith("\Datas\Database"):
    pass
else:
    os.chdir("Project/Datas/Database")
# ---------------------------------

conn = sql.connect("database.db")
cur = conn.cursor()
# Estate Database Module
# --------------------------------------------------


def estate_new(owner_name: str, owner_id: int, price: int, bedrooms: int, area: int, storage_room: int, garage: int, year_built: str, active: bool = True):
    estate = (owner_name, owner_id, price,
              bedrooms, area, storage_room, garage, year_built, active)
    cur.execute("INSERT INTO estates VALUES(?,?,?,?,?,?,?,?,?)", estate)
    conn.commit()


def estate_update_activation(id: int):
    cur.execute(f"""--sql
    UPDATE estates SET activation = NULL WHERE rowid = {id}
    ;""")
    conn.commit()

# TODO ye kari konam bere bar asase owner_name va owner_last name search kone idish ro peyda kone


def estate_datas():  # function to print database
    cur.execute("SELECT * FROM estates WHERE activation IS NOT NULL")
    estates = cur.fetchall()
    for estate in estates:
        print(estate)


# -------------------------------------------------
