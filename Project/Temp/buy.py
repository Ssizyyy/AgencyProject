import pandas as pd
import os

data = pd.read_csv("DataBase.csv")


class Request_Buy:
    def __init__(self, budget=None, bedrooms=None, area=None, year_built=None) -> None:
        self.budget = budget
        self.bedrooms = bedrooms
        self.area = area
        self.year_built = year_built

    def search(self):
        print(data)
        self.search_budget()
        print(self.filtered)
        self.search_bedrooms()
        print(self.filtered)
        self.search_area()
        print(self.filtered)
        self.search_year_built()
        print(self.filtered)
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
            print(data[(data.Price >= lower)
                                 & (data.Price <= higher)])
            self.filtered = data[(data.Price >= lower)
                                 & (data.Price <= higher)]
        else:
            budget = int("".join(self.budget.split()))
            self.filtered = data[(data.Price == budget)]

    def search_bedrooms(self):
        if self.bedrooms == None:
            pass#self.filtered = self.filtered
        if self.bedrooms.endswith(">"):
            bedrooms = self.bedrooms.strip()
            bedrooms = bedrooms[:-1]
            bedrooms = int(bedrooms)
            print(bedrooms)
            self.filtered = self.filtered[(self.filtered.Bedrooms >= bedrooms)]
        elif self.bedrooms.endswith("<"):
            bedrooms = self.bedrooms.strip()
            bedrooms = bedrooms[:-1]
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
            pass#self.filtered = self.filtered
        if self.area.endswith(">"):
            area = self.area.strip()
            area = area[:-1]
            area = int(area)
            self.filtered = self.filtered[(self.filtered.Area >= area)]
        elif self.area.endswith("<"):
            area = self.area.strip()
            area = area[:-1]
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
            pass#self.filtered = self.filtered
        if self.year_built.endswith(">"):
            year_built = self.year_built.strip()
            year_built = year_built[:-1]
            year_built = int(year_built)
            self.filtered = self.filtered[(self.filtered.YearBuilt >= year_built)]
        elif self.year_built.endswith("<"):
            year_built = self.year_built.strip()
            year_built = year_built[:-1]
            year_built = int(year_built)
            self.filtered = self.filtered[(self.filtered.YearBuilt <= year_built)]
        elif "-" in self.year_built:
            lower, higher = self.year_built.split("-")
            lower = int("".join(lower.split()))
            higher = int("".join(higher.split()))
            self.filtered = self.filtered[(self.filtered.YearBuilt >= lower)
                                 & (self.filtered.YearBuilt <= higher)]
        else:
            year_built = int("".join(self.year_built.split()))
            self.filtered = self.filtered[(self.filtered.YearBuilt == year_built)]


# mmd = Request_Buy("300-500","1-3","70-150","2000-2020")
# mmd.search()
# print(mmd.filtered)
# print(data[(data.Price < 300)])
