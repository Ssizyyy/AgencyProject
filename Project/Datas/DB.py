import os
import pandas as pd


#Person Functions
#Creating DB File
#--------------------------------------------------
os.chdir("Datas")
if os.path.exists("DataBase.csv"):
    pass
else:
    f = open("DataBase.csv","x")
    f.close()
    df = pd.DataFrame(columns=["ID","FirstName","LastName","NationalCode","Birthdate","OverallBudget"])
    df.to_csv("DataBase.csv",index=False)
#--------------------------------------------------
#--------------------------------------------------
def person_ID():
    df = pd.read_csv("DataBase.csv",delimiter=",")
    if df.empty:
        return 0
    else:
        last_id = df.iloc[-1][0]
        return int(last_id)+1
def new_person(f_name: str,l_name: str,national_code: str,birthdate: str,overall_budget: str):
    ID = person_ID()
    person = [ID,f_name,l_name,national_code,birthdate,overall_budget]
    df = pd.read_csv("DataBase.csv",delimiter=",")
    df.loc[len(df)] = person
    df.to_csv("DataBase.csv",index=False)
def person_datas():
    df = pd.read_csv("DataBase.csv",delimiter=",")
    print(df.to_string())
def remove_person():
    pass
#---------------------------------------------------


# mmd.Customers.new_person(mmd,"mmd","mmd","mmd","mmd","mmd")
# mmd.Customers.show_datas(mmd)
# print(person_ID())
# df = pd.read_csv("Database.csv")
# print(df)