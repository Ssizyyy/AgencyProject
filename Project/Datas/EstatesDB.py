import pandas as pd
import os

# Switching Working Directory
# ----------------------------------
if os.getcwd().endswith("\Datas\Database"):
    pass
else:
    os.chdir("Project/Datas/Database")
# ---------------------------------
if os.path.exists("EstatesDB.csv"): # check if we have database or not
    pass
else:
    df = pd.DataFrame(columns=["ID", "Owner's Name", "Owner's ID", "Price", "Bedrooms",
                               "Area", "StorageRoom", "Garage", "YearBuilt","Active"])
    df.to_csv("EstatesDB.csv", index=False)
# --------------------------------------------------


# Estate Database Module
# --------------------------------------------------
def estate_id(): # function to return next id
    df = pd.read_csv("EstatesDB.csv", delimiter=",")
    if df.empty:
        return 0
    else:
        last_id = df.iloc[-1][0]
        return int(last_id)+1

# function to define new estate in database
def estate_new(owners_name: str, owners_id: int, price: int, bedrooms: int, area: int, storage_room: int, garage: int, year_built: str,active:bool = True):
    id = estate_id()
    estate = [id, owners_name, owners_id, price,
              bedrooms, area, storage_room, garage, year_built,active]
    df = pd.read_csv("EstatesDB.csv", delimiter=",")
    df.loc[len(df)] = estate
    df.to_csv("EstatesDB.csv", index=False)


def estate_datas(): # function to print database
    df = pd.read_csv("EstatesDB.csv", delimiter=",")
    print(df.to_string())


def estate_remove(id): #function to remove a data by giving ID
    df = pd.read_csv("EstatesDB.csv", delimiter=",")
    selection = df.loc[df["ID"] == id].index
    df = df.drop(selection)
    df.to_csv("EstatesDB.csv", index=False)


# -------------------------------------------------
#! function baraye change active boodan ya naboodan
