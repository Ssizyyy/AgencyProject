import os
import pandas as pd


# Switching Working Directory
# ----------------------------------
if os.getcwd().endswith("\Datas\Database"):
    pass
else:
    os.chdir("Project/Datas/Database")
# ---------------------------------
# Creating DB File
# --------------------------------------------------
if os.path.exists("AdminsDB.csv"):
    pass
else:
    # f = open("AdminsDB.csv", "x")
    # f.close()
    df = pd.DataFrame(columns=["ID", "FirstName", "LastName",
                               "Username", "Password", "Nationa Code", "Birthdate", "Gender"])
    df.to_csv("AdminsDB.csv", index=False)
# --------------------------------------------------


# Admins Database Module
# --------------------------------------------------
def admin_ID():
    df = pd.read_csv("AdminsDB.csv", delimiter=",")
    if df.empty:
        return 0
    else:
        last_id = df.iloc[-1][0]
        return int(last_id)+1


def admin_new(f_name: str, l_name: str, username: str, password: str, national_code: str, birthdate: str, gender: str):
    id = admin_ID()
    admin = [id, f_name, l_name, username, password, national_code,
             birthdate, gender]
    df = pd.read_csv("AdminsDB.csv", delimiter=",")
    df.loc[len(df)] = admin
    df.to_csv("AdminsDB.csv", index=False)


def admin_datas():
    df = pd.read_csv("AdminsDB.csv", delimiter=",")
    print(df.to_string())


def admin_remove(id):
    df = pd.read_csv("AdminsDB.csv", delimiter=",")
    selection = df.loc[df["ID"] == id].index
    df = df.drop(selection)
    df.to_csv("AdminsDB.csv", index=False)
# ---------------------------------------------------
