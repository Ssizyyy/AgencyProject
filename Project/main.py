import os
import csv
import Datas.DB as DB


class Agency:
    pass




class Customer:
    def __init__(self,f_name = None,l_name= None,natioal_code = None,birthdate = None,overall_budget = None):
        self.ID = DB.person_ID()
        self.f_name = f_name
        self.l_name = l_name
        self.natioal_code = natioal_code
        self.birthdate = birthdate
        self.overall_budget = overall_budget
        DB.new_person(f_name,l_name,natioal_code,birthdate,overall_budget)

mmd = Customer("hossein","salehi","8569","1/1/2000","35000")




class Estate:
    def __init__(self):
        pass




class Admin:
    def __init__(self):
        pass

class Buy:
    def __init__(self,budget,rooms) -> None:
        self.budget = budget
        self.rooms = rooms
class Sell:
    pass





class Trade(Buy,Sell):
    def __init__():
        pass
    #moshakhas kardane Noe darkhast


class DataBase:
    pass
    #https://www.codingem.com/python-write-to-csv-file/
    #https://realpython.com/python-csv/