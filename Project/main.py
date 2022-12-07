import os
import csv
import Datas.CustomersDB
import Datas.EstatesDB
import Datas.AdminsDB


class Agency:
    pass


class Admin:
    def __init__(self, f_name: str, l_name: str, username: str, password: str, national_code: str, birthdate: str, gender: str):
        self.id = Datas.AdminsDB.admin_ID()
        self.f_name = f_name
        self.l_name = l_name
        self.username = username
        self.password = password
        self.nationa_code = national_code
        self.birthdate = birthdate
        self.gender = gender
        Datas.AdminsDB.admin_new(
            f_name, l_name, username, password, national_code, birthdate, gender)




class Customer:
    def __init__(self, f_name: str, l_name: str, natioal_code: str, birthdate: str, gender: str, overall_budget: int) -> None:
        self.id = Datas.CustomersDB.customer_ID()
        self.f_name = f_name
        self.l_name = l_name
        self.natioal_code = natioal_code
        self.birthdate = birthdate
        self.gender = gender
        self.overall_budget = overall_budget
        Datas.CustomersDB.customer_new(
            f_name, l_name, natioal_code, birthdate, gender, overall_budget)
    #! function hash kamel nist


# mmd = Customer("hossein", "salehi", "8569", "1/1/2000", "Male" , 35000)


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
        Datas.EstatesDB.estate_new(
            owners_name, owners_id, price, bedrooms, area, storage_room, garage, year_built)
        #!function hash kamel nist

# mmd = Estate("mmd",1,2000,2,130,1,1,1987)


class Request_Buy:
    def __init__(self,budget=None,bedrooms=None,area=None,year_built=None) -> None:
        pass


class Request_Sell(Estate):
    def __init__(self, owners_name: str, owners_id: int, price: int, bedrooms: int, area: int, storage_room: int, garage: int, year_built: str) -> None:
        super().__init__(owners_name, owners_id, price,
                         bedrooms, area, storage_room, garage, year_built)


class Trade():
    def __init__():
        pass
    # moshakhas kardane Noe darkhast


class DataBase:
    pass
    # https://www.codingem.com/python-write-to-csv-file/
    # https://realpython.com/python-csv/

    
    #https://www.listendata.com/2019/07/how-to-filter-pandas-dataframe.html



#TODO be header custoemra "Estates" ezafe konam va har estate jadidi ke sakhte mishe IDsh bere be "Estates" add she