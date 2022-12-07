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
        self.id = buyreq_id()
        self.budget = budget
        self.bedrooms = bedrooms
        self.area = area
        self.year_built = year_built
        buyreq_new(budget, bedrooms, area, year_built)

    @classmethod
    def search(self):
        self.search_budget(self)
        self.search_bedrooms(self)
        self.search_area(self)
        self.search_year_built(self)
        print("_____________________________________")
        print(
            f"Request: \n{self.df.iloc[self.requests_counter].to_string()}")
        print()
        print("Match Estates:")
        print(self.filtered.to_string(index=False))
        ids = []
        for row in range(self.filtered.shape[0]):
            ids.append(self.filtered.iloc[row][0])
        if len(ids) == 0:
            print("There's No Match Estate")
        else:
            print("Request ID", self.requests_counter,
                  "Matches With IDs :", *ids, " In Estates")
        self.requests_counter += 1
        print("")
        print("_____________________________________")

    @classmethod
    def search_full(self):
        self.df = pd.read_csv("BuyRequestsDB.csv")
        self.requests_counter = 0
        for reqs in range(buyreq_id()):
            self.budget = self.df.iloc[reqs][1]
            self.bedrooms = self.df.iloc[reqs][2]
            self.area = self.df.iloc[reqs][3]
            self.year_built = self.df.iloc[reqs][4]
            Request_Buy.search()

    def search_budget(self):
        self.budget = str(self.budget)
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
        self.bedrooms = str(self.bedrooms)
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
        self.area = str(self.area)
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
        self.year_built = str(self.year_built)
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


def match_estate(reqest_id: int, estate_id: int):
    estate_data = pd.read_csv("EstatesDB.csv")
    requests_data = pd.read_csv("BuyRequestsDB.csv")
    estate_data_selection = estate_data.loc[estate_data["ID"] == estate_id].index
    requests_data_selection = requests_data.loc[requests_data["ID"] == reqest_id].index
    estate_data = estate_data.drop(estate_data_selection)
    requests_data = requests_data.drop(requests_data_selection)
    estate_data.to_csv("EstatesDB.csv", index=False)
    requests_data.to_csv("BuyRequestsDB.csv", index=False)

# 3000,5,1000,1,1,2020
# new_req = Request_Buy("3000","5","1000","2020")



Request_Buy.search_full()



#TODO ye header "Active Status" add konam va match kardano ba active boodan ya naboodan neshoon bedam
#TODO data i ke bala taarif kardam ro ham filter mikonam faghat oonaii ke active == yes hastan

#TODO ye database joda bara save kardan ID haii ke be ham match shodan

#TODO ye def match(id1,id2) bara admin ha sakhte she
#TODO ye def match() bara moghei ke search mikonim be karbar entekhab bede ke az beyne chand ta estate i ke match mishan ba request select kone