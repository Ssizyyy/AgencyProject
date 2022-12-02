import os
import pandas as pd


# Person Functions
# Creating DB File
# --------------------------------------------------
# Switching Working Directory
# ----------------------------------
if os.getcwd().endswith("\Datas\Database"):
    pass
else:
    os.chdir("Project/Datas/Database")
# ---------------------------------
if os.path.exists("CustomersDB.csv"):
    pass
else:
    # f = open("CustomersDB.csv", "x")
    # f.close()
    df = pd.DataFrame(columns=["ID", "FirstName", "LastName",
                               "NationalCode", "Birthdate", "OverallBudget"])
    df.to_csv("CustomersDB.csv", index=False)
# --------------------------------------------------
# --------------------------------------------------


def customer_ID():
    df = pd.read_csv("CustomersDB.csv", delimiter=",")
    if df.empty:
        return 0
    else:
        last_id = df.iloc[-1][0]
        return int(last_id)+1


def customer_new(f_name: str, l_name: str, national_code: str, birthdate: str, overall_budget: str):
    id = customer_ID()
    person = [id, f_name, l_name, national_code, birthdate, overall_budget]
    df = pd.read_csv("CustomersDB.csv", delimiter=",")
    df.loc[len(df)] = person
    df.to_csv("CustomersDB.csv", index=False)


def customer_datas():
    df = pd.read_csv("CustomersDB.csv", delimiter=",")
    print(df.to_string())


def customer_remove(id):
    df = pd.read_csv("CustomersDB.csv", delimiter=",")
    selection = df.loc[df["ID"] == id].index
    df = df.drop(selection)
    df.to_csv("CustomersDB.csv", index=False)
# ---------------------------------------------------
