import pandas as pd
import os

file = pd.read_csv("mmd.csv")

class Request_Buy:
    def __init__(self,budget=None,bedrooms=None,area=None,year_built=None) -> None:
        self.budget = budget
        self.bedrooms = bedrooms
        self.area = area
        self.year_built = year_built
    def search_budget(self):
        if self.budget.find(">") == 1:
            file[(file.budget>self.budget)]
