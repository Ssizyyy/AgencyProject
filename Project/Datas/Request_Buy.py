import pandas as pd
import os


# ----------------------------------
# Switching Working Directory
if os.getcwd().endswith("\Datas\Database"):
    pass
else:
    os.chdir("Project/Datas/Database")
# ---------------------------------
# Reading Esates Database
if os.path.exists("EstatesDB.csv"):
    data = pd.read_csv("EstatesDB.csv")
else:
    print("Database not Found !")
# ---------------------------------
# Creating BuyReqs Database
if os.path.exists("BuyRequestsDB.csv"):
    pass
else:
    df = pd.DataFrame(
        columns=["ID", "Budget", "Bedrooms", "Area", "YearBuilt"])
    df.to_csv("BuyRequestsDB.csv", index=False)

# -------------------------------------------------
# DB functions
# -------------------------------------------------


def buyreq_id():
    df = pd.read_csv("BuyRequestsDB.csv")
    if df.empty:
        return 0
    else:
        last_id = df.iloc[-1][0]
        return int(last_id)+1


def buyreq_new(budget: str, bedrooms: str, area: str, year_built: str):
    id = buyreq_id()
    df = pd.read_csv("BuyRequestsDB.csv")
    buyreq = [id, budget, bedrooms, area, year_built]
    df.loc[len(df)] = buyreq
    df.to_csv("BuyRequestsDB.csv", index=False)


def buyreq_show():
    df = pd.read_csv("BuyRequestsDB.csv")
    print(df.to_string())


def buyreq_remove(id):
    df = pd.read_csv("BuyRequestsDB.csv")
    selection = df[(df.ID == id)]
    df.drop(selection)
    df.to_csv("BuyRequestsDB.csv", index=False)

# ---------------------------------------------------------------


class Request_Buy:
    def __init__(self, budget: str = None, bedrooms: str = None, area: str = None, year_built: str = None) -> None:
        self.budget = budget
        self.bedrooms = bedrooms
        self.area = area
        self.year_built = year_built
        if "DNS" in budget:
            pass
        else:
            buyreq_new(budget, bedrooms, area, year_built)

    def search(self):
        self.search_budget()
        self.search_bedrooms()
        self.search_area()
        self.search_year_built()
        print(self.filtered)

    def search_full(self):
        df = pd.read_csv("BuyRequestsDB.csv")
        for reqs in range(buyreq_id()):
            self.budget = df.iloc[reqs][1]
            self.bedrooms = df.iloc[reqs][2]
            self.area = df.iloc[reqs][3]
            self.year_built = df.iloc[reqs][4]
            self.search()

            pass

    def search_budget(self):
        if self.budget == None:
            self.filtered = data
        if self.budget.endswith(">"):
            budget = self.budget.strip()
            budget = budget[:-1]
            budget = int(budget)
            self.filtered = data[(data.Price >= budget)]
        elif self.budget.endswith("<"):
            budget = self.budget.strip()
            budget = budget[:-1]
            budget = int(budget)
            self.filtered = data[(data.Price <= budget)]
        elif "-" in self.budget:
            lower, higher = self.budget.split("-")
            lower = int("".join(lower.split()))
            higher = int("".join(higher.split()))
            self.filtered = data[(data.Price >= lower)
                                 & (data.Price <= higher)]
        else:
            budget = int("".join(self.budget.split()))
            self.filtered = data[(data.Price == budget)]

    def search_bedrooms(self):
        if self.bedrooms == None:
            pass  # self.filtered = self.filtered
        if self.bedrooms.endswith(">"):
            bedrooms = self.bedrooms.strip()
            bedrooms = bedrooms[: -1]
            bedrooms = int(bedrooms)
            self.filtered = self.filtered[(self.filtered.Bedrooms >= bedrooms)]
        elif self.bedrooms.endswith("<"):
            bedrooms = self.bedrooms.strip()
            bedrooms = bedrooms[: -1]
            bedrooms = int(bedrooms)
            self.filtered = self.filtered[(self.filtered.Bedrooms <= bedrooms)]
        elif "-" in self.bedrooms:
            lower, higher = self.bedrooms.split("-")
            lower = int("".join(lower.split()))
            higher = int("".join(higher.split()))
            self.filtered = self.filtered[(self.filtered.Bedrooms >= lower)
                                          & (self.filtered.Bedrooms <= higher)]
        else:
            bedrooms = int("".join(self.bedrooms.split()))
            self.filtered = self.filtered[(self.filtered.Bedrooms == bedrooms)]

    def search_area(self):
        if self.area == None:
            pass  # self.filtered = self.filtered
        if self.area.endswith(">"):
            area = self.area.strip()
            area = area[: -1]
            area = int(area)
            self.filtered = self.filtered[(self.filtered.Area >= area)]
        elif self.area.endswith("<"):
            area = self.area.strip()
            area = area[: -1]
            area = int(area)
            self.filtered = self.filtered[(self.filtered.Area <= area)]
        elif "-" in self.area:
            lower, higher = self.area.split("-")
            lower = int("".join(lower.split()))
            higher = int("".join(higher.split()))
            self.filtered = self.filtered[(self.filtered.Area >= lower)
                                          & (self.filtered.Area <= higher)]
        else:
            area = int("".join(self.area.split()))
            self.filtered = self.filtered[(self.filtered.Area == area)]

    def search_year_built(self):
        if self.year_built == None:
            pass  # self.filtered = self.filtered
        if self.year_built.endswith(">"):
            year_built = self.year_built.strip()
            year_built = year_built[: -1]
            year_built = int(year_built)
            self.filtered = self.filtered[(
                self.filtered.YearBuilt >= year_built)]
        elif self.year_built.endswith("<"):
            year_built = self.year_built.strip()
            year_built = year_built[: -1]
            year_built = int(year_built)
            self.filtered = self.filtered[(
                self.filtered.YearBuilt <= year_built)]
        elif "-" in self.year_built:
            lower, higher = self.year_built.split("-")
            lower = int("".join(lower.split()))
            higher = int("".join(higher.split()))
            self.filtered = self.filtered[(self.filtered.YearBuilt >= lower)
                                          & (self.filtered.YearBuilt <= higher)]
        else:
            year_built = int("".join(self.year_built.split()))
            self.filtered = self.filtered[(
                self.filtered.YearBuilt == year_built)]


#3000,5,1000,1,1,2020
new_req = Request_Buy("3000","5","1000","2020")

mmd =Request_Buy("DNS")
mmd.search_full()