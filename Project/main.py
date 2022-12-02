import os
import csv
import Datas.CustomersDB
import Datas.EstatesDB

class Agency:
    pass


class Customer:
    def __init__(self, f_name, l_name, natioal_code, birthdate, overall_budget) -> None:
        self.id = Datas.CustomersDB.customer_ID()
        self.f_name = f_name
        self.l_name = l_name
        self.natioal_code = natioal_code
        self.birthdate = birthdate
        self.overall_budget = overall_budget
        Datas.CustomersDB.customer_new(
            f_name, l_name, natioal_code, birthdate, overall_budget)
    #! function hash kamel nist

mmd = Customer("hossein","salehi","8569","1/1/2000","35000")


class Estate:
    def __init__(self, owners_name: str, owners_id: int, price: int, bedrooms: int, area: int, storage_room: int, garage: int, year_built: str) -> None:
        self.id = Datas.EstatesDB.estate_id()
        self.owners_name = owners_name
        self.owners_id = owners_id
        self.price = price
        self.bedrooms = bedrooms
        self.area = area
        self.storage_room = storage_room
        self.garage = garage
        self.year_built = year_built
        Datas.EstatesDB.estate_new(owners_name,owners_id,price,bedrooms,area,storage_room,garage,year_built)
        #!function hash kamel nist

# mmd = Estate("mmd",1,2000,2,130,1,1,1987)

class Admin:
    def __init__(self):
        pass


class Buy:
    pass


class Sell(Estate):
    def __init__(self, owners_name: str, owners_id: int, price: int, bedrooms: int, area: int, storage_room: int, garage: int, year_built: str) -> None:
        super().__init__(owners_name, owners_id, price, bedrooms, area, storage_room, garage, year_built)


class Trade():
    def __init__():
        pass
    # moshakhas kardane Noe darkhast


class DataBase:
    pass
    # https://www.codingem.com/python-write-to-csv-file/
    # https://realpython.com/python-csv/