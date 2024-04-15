import sqlite3 as sql
import os


# ----------------------------------
# Switching Working Directory
# if os.getcwd().endswith("\Datas\Database"): #!FIXME ino az comment dar biaram
#     pass
# else:
#     os.chdir("Project/Datas/Database")
# ---------------------------------
# Request DB functions
# -------------------------------------------------

def buyreq_new(budget: int, bedrooms: int, area: int, year_built: int, address: str, activation: bool):
    lst = (budget, bedrooms, area, year_built, address, activation)

    conn = sql.connect('database.db')
    cur = conn.cursor()
    cur.execute("""--sql
    INSERT INTO requests VALUES (?,?,?,?,?,?)    
    ;""", lst)
    conn.commit()
    conn.close()


def buyreq_show():
    conn = sql.connect("database.db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM requests WHERE activation NOT NULL")
    print(cur.fetchall())
# ---------------------------------------------------------------

# MathedEstates DB functions
# -------------------------------------------------


def database_match_new(*args):

    lst = (args[0], args[1], args[2], args[3], args[4], args[5], args[6], args[7],
           args[8], args[9], args[10], args[11], args[12], args[13], args[14])
    conn = sql.connect("database.db")
    cur = conn.cursor()
    cur.execute("""--sql
    INSERT INTO mathed VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    ;""", lst)
    conn.commit()
    conn.close()


# -------------------------------------------------
class Request_Buy:
    def __init__(self, budget: str = None, bedrooms: str = None, area: str = None, year_built: str = None, address: str = None, active: bool = True) -> None:
        self.budget = budget
        self.bedrooms = bedrooms
        self.area = area
        self.year_built = year_built
        self.address = address
        self.active = active
        buyreq_new(budget, bedrooms, area, year_built, address, active)

    @classmethod
    def search(self):

        global conn,cur
        conn = sql.connect('database.db')
        cur = conn.cursor()







        global temp_conn,temp_cur

        temp_conn = sql.connect(':memory:')
        temp_cur = temp_conn.cursor()
        temp_cur.execute(
            """--sql
                    CREATE TABLE IF NOT EXISTS temp_budget(
                        owner_id text,
                        owner_name text,
                        price int,
                        bedrooms int,
                        area int,
                        storage_room int,
                        garage int,
                        year_built int,
                        activation null
                    )
                    ;""")

        temp_cur.execute(
            """--sql
                    CREATE TABLE IF NOT EXISTS temp_bedrooms(
                        owner_id text,
                        owner_name text,
                        price int,
                        bedrooms int,
                        area int,
                        storage_room int,
                        garage int,
                        year_built int,
                        activation null
                    )
                    ;""")


        temp_cur.execute(
            """--sql
                    CREATE TABLE IF NOT EXISTS temp_area(
                        owner_id text,
                        owner_name text,
                        price int,
                        bedrooms int,
                        area int,
                        storage_room int,
                        garage int,
                        year_built int,
                        activation null
                    )
                    ;""")

        temp_cur.execute(
            """--sql
                    CREATE TABLE IF NOT EXISTS temp_year_built(
                        owner_id text,
                        owner_name text,
                        price int,
                        bedrooms int,
                        area int,
                        storage_room int,
                        garage int,
                        year_built int,
                        activation null
                    )
                    ;""")


        
        self.search_budget(self)
        self.search_bedrooms(self)
        self.search_area(self)
        self.search_year_built(self)
        temp_cur.execute("SELECT * FROM temp_year_built")
        return temp_cur.fetchall()
        # print("_____________________________________")
        # print(
        #     f"Request: \n{self.df.iloc[self.requests_counter].to_string()}")
        # print()
        # print("Match Estates:")
        # if self.filtered.empty:
        #     pass
        # else:
        #     print(self.filtered.to_string(index=False))
        # ids = []
        # for row in range(self.filtered.shape[0]):
        #     ids.append(self.filtered.iloc[row][0])
        # if len(ids) == 0:
        #     print("There's No Match Estate")
        # else:
        #     print("Request ID", self.df.iloc[self.requests_counter][0],
        #           "Matches With IDs :", *ids, " In Estates")
        # self.requests_counter += 1
        # print("")
        # print("_____________________________________")

    @classmethod
    def search_full(self):

        conn = sql.connect("database.db")
        cur = conn.cursor()
        cur.execute("SELECT * FROM requests")
        reqs = cur.fetchall()

        # iterating buyrequests ,self.df.shape[0] == row count

        result_list = []

        for req in reqs:
            self.budget = req[0]
            self.bedrooms = req[1]
            self.area = req[2]
            self.year_built = req[3]
            result_list.append(Request_Buy.search())
        print(result_list)

    def search_budget(self):

        if self.budget == None:
            cur.execute("SELECT * FROM estates")
            lst = temp_cur.fetchall()
            temp_cur.executemany("INSERT INTO temp_budget VALUES(?,?,?,?,?,?,?,?,?)", lst)

        elif self.budget.endswith(">"):
            budget = str(self.budget)
            budget = self.budget.strip()
            budget = budget[: -1]
            budget = int(budget)

            cur.execute(f"""--sql
            SELECT * FROM estates WHERE price >= {budget}
            ;""")

            lst = cur.fetchall()

            temp_cur.executemany(
                """--sql
                    INSERT INTO temp_budget VALUES(?,?,?,?,?,?,?,?,?)
                    ;""", lst)
            #!khodaya komakkkkkkkkkkkk
        elif self.budget.endswith("<"):
            budget = str(self.budget)
            budget = self.budget.strip()
            budget = budget[: -1]
            budget = int(budget)

            cur.execute(f"""--sql
            SELECT * FROM estates WHERE price <= {budget}
            ;""")
            lst = cur.fetchall()

            temp_cur.executemany(
                """--sql
                    INSERT INTO temp_budget VALUES(?,?,?,?,?,?,?,?,?)
                    ;""", lst)
        elif "-" in self.budget:
            budget = str(self.budget)
            lower, higher = self.budget.split("-")
            lower = int("".join(lower.split()))
            higher = int("".join(higher.split()))

            cur.execute(f"""--sql
            SELECT * FROM estates WHERE price BETWEEN {lower} AND {higher}
            ;""")
            lst = cur.fetchall()

            temp_cur.executemany(
                """--sql
                    INSERT INTO temp_budget VALUES(?,?,?,?,?,?,?,?,?)
                    ;""", lst)

        else:
            budget = str(self.budget)
            budget = int("".join(self.budget.split()))

            cur.execute(f"""--sql
            SELECT * FROM estates WHERE price = {budget}
            ;""")
            lst = cur.fetchall()

            temp_cur.executemany(
                """--sql
                    INSERT INTO temp_budget VALUES(?,?,?,?,?,?,?,?,?)
                    ;""", lst)

    def search_bedrooms(self):    
        if self.bedrooms == None:
            temp_cur.execute("SELECT * FROM temp_budget")
            lst = temp_cur.fetchall()
            temp_cur.executemany("INSERT INTO temp_bedrooms VALUES(?,?,?,?,?,?,?,?,?)", lst)
            print("none e")
        elif self.bedrooms.endswith(">"):
            bedrooms = str(self.bedrooms)
            bedrooms = self.bedrooms.strip()
            bedrooms = bedrooms[: -1]
            bedrooms = int(bedrooms)
            temp_cur.execute(f"""--sql
            SELECT * FROM temp_budget WHERE bedrooms >= {bedrooms}
            ;""")
            lst = temp_cur.fetchall()

            temp_cur.executemany(
                """--sql
                    INSERT INTO temp_bedrooms VALUES(?,?,?,?,?,?,?,?,?)
                    ;""", lst)

        elif self.bedrooms.endswith("<"):
            bedrooms = str(self.bedrooms)
            bedrooms = self.bedrooms.strip()
            bedrooms = bedrooms[: -1]
            bedrooms = int(bedrooms)

            temp_cur.execute(f"""--sql
            SELECT * FROM temp_budget WHERE bedrooms <= {bedrooms}
            ;""")
            lst = temp_cur.fetchall()

            temp_cur.executemany(
                """--sql
                    INSERT INTO temp_bedrooms VALUES(?,?,?,?,?,?,?,?,?)
                    ;""", lst)

        elif "-" in self.bedrooms:
            bedrooms = str(self.bedrooms)
            lower, higher = self.bedrooms.split("-")
            lower = int("".join(lower.split()))
            higher = int("".join(higher.split()))

            temp_cur.execute(f"""--sql
            SELECT * FROM temp_budget WHERE bedrooms BETWEEN {lower} AND {higher}
            ;""")
            lst = temp_cur.fetchall()

            temp_cur.executemany(
                """--sql
                    INSERT INTO temp_bedrooms VALUES(?,?,?,?,?,?,?,?,?)
                    ;""", lst)

        else:
            bedrooms = str(self.bedrooms)
            bedrooms = int("".join(self.bedrooms.split()))

            temp_cur.execute(f"""--sql
            SELECT * FROM temp_budget WHERE bedrooms = {bedrooms}
            ;""")
            lst = temp_cur.fetchall()

            temp_cur.executemany(
                """--sql
                    INSERT INTO temp_bedrooms VALUES(?,?,?,?,?,?,?,?,?)
                    ;""", lst)

    def search_area(self):

        if self.area == None:
            temp_cur.execute("SELECT * FROM temp_bedrooms")
            lst = temp_cur.fetchall()
            temp_cur.executemany("INSERT INTO temp_area VALUES(?,?,?,?,?,?,?,?,?)", lst)
        elif self.area.endswith(">"):
            area = str(self.area)
            area = self.area.strip()
            area = area[: -1]
            area = int(area)
            temp_cur.execute(f"""--sql
            SELECT * FROM temp_bedrooms WHERE area >= {area}
            ;""")
            lst = temp_cur.fetchall()

            temp_cur.executemany(
                """--sql
                    INSERT INTO temp_area VALUES(?,?,?,?,?,?,?,?,?)
                    ;""", lst)
        elif self.area.endswith("<"):
            area = str(self.area)
            area = self.area.strip()
            area = area[: -1]
            area = int(area)
            temp_cur.execute(f"""--sql
            SELECT * FROM temp_bedrooms WHERE area <= {area}
            ;""")
            lst = temp_cur.fetchall()

            temp_cur.executemany(
                """--sql
                    INSERT INTO temp_area VALUES(?,?,?,?,?,?,?,?,?)
                    ;""", lst)
        elif "-" in self.area:
            area = str(self.area)
            lower, higher = self.area.split("-")
            lower = int("".join(lower.split()))
            higher = int("".join(higher.split()))
            temp_cur.execute(f"""--sql
            SELECT * FROM temp_bedrooms WHERE area BETWEEN {lower} AND {higher}
            ;""")
            lst = temp_cur.fetchall()

            temp_cur.executemany(
                """--sql
                    INSERT INTO temp_area VALUES(?,?,?,?,?,?,?,?,?)
                    ;""", lst)
        else:
            area = str(self.area)
            area = int("".join(self.area.split()))
            temp_cur.execute(f"""--sql
            SELECT * FROM temp_bedrooms WHERE area = {area}
            ;""")
            lst = temp_cur.fetchall()

            temp_cur.executemany(
                """--sql
                    INSERT INTO temp_area VALUES(?,?,?,?,?,?,?,?,?)
                    ;""", lst)

    def search_year_built(self):
        
        if self.year_built == None:
            temp_cur.execute("SELECT * FROM temp_area")
            lst = temp_cur.fetchall()
            temp_cur.executemany("INSERT INTO temp_year_built VALUES(?,?,?,?,?,?,?,?,?)", lst)

        elif self.year_built.endswith(">"):
            year_built = str(self.year_built)
            year_built = self.year_built.strip()
            year_built = year_built[: -1]
            year_built = int(year_built)
            temp_cur.execute(f"""--sql
            SELECT * FROM temp_area WHERE year_built >= {year_built}
            ;""")
            lst = temp_cur.fetchall()

            temp_cur.executemany(
                """--sql
                    INSERT INTO temp_year_built VALUES(?,?,?,?,?,?,?,?,?)
                    ;""", lst)
        elif self.year_built.endswith("<"):
            year_built = str(self.year_built)
            year_built = self.year_built.strip()
            year_built = year_built[: -1]
            year_built = int(year_built)

            temp_cur.execute(f"""--sql
            SELECT * FROM temp_area WHERE year_built <= {year_built}
            ;""")
            lst = temp_cur.fetchall()

            temp_cur.executemany(
                """--sql
                    INSERT INTO temp_year_built VALUES(?,?,?,?,?,?,?,?,?)
                    ;""", lst)

        elif "-" in self.year_built:
            year_built = str(self.year_built)
            lower, higher = self.year_built.split("-")
            lower = int("".join(lower.split()))
            higher = int("".join(higher.split()))
            temp_cur.execute(f"""--sql
            SELECT * FROM temp_area WHERE year_built BETWEEN {lower} AND {higher}
            ;""")
            lst = temp_cur.fetchall()

            temp_cur.executemany(
                """--sql
                    INSERT INTO temp_year_built VALUES(?,?,?,?,?,?,?,?,?)
                    ;""", lst)
        else:
            year_built = str(self.year_built)
            year_built = int("".join(self.year_built.split()))

            temp_cur.execute(f"""--sql
            SELECT * FROM temp_area WHERE year_built = {year_built}
            ;""")
            lst = temp_cur.fetchall()

            temp_cur.executemany(
                """--sql
                    INSERT INTO temp_year_built VALUES(?,?,?,?,?,?,?,?,?)
                    ;""", lst)


def change_active_status_estate(estate_id: int):
    conn = sql.connect("database.db")
    cur = conn.cursor()
    cur.execute(f"UPDATE estates SET activations=NULL WHERE rowid={estate_id}")


def change_active_status_request(request_id: int):
    conn = sql.connect("database.db")
    cur = conn.cursor()
    cur.execute(f"UPDATE requests SET activations=NULL WHERE rowid={request_id}")


def match_estate_request(request_id: int, estate_id: int):
    change_active_status_request(request_id)
    change_active_status_estate(estate_id)

    conn = sql.connect("database.db")
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM requests WHERE rowid={request_id}")
    request = cur.fetchone()
    cur.execute(f"SELECT * FROM estates WHERE rowid={estate_id}")
    estate = cur.fetchone()
    print("Estate :")
    print(estate)
    print("Mathed With :")
    print(request)

#! ta inja neveshtam ke request o match mikone

# 3000,5,1000,1,1,2020
# new_req = Request_Buy("3000","5","1000","2020")


# Request_Buy.search_full()


# 1
# TODO ye header "Active Status" add konam va match kardano ba active boodan ya naboodan neshoon bedam
# TODO data i ke bala taarif kardam ro ham filter mikonam faghat oonaii ke active == yes hastan
# Here
# 2
# TODO ye database joda bara save kardan ID haii ke be ham match shodan
# 3
# TODO ye def match(id1,id2) bara admin ha sakhte she
# TODO ye def match() bara moghei ke search mikonim be karbar entekhab bede ke az beyne chand ta estate i ke match mishan ba request select kone


# mmd = Request_Buy("300>","1","130","20000101")
# print()
print(Request_Buy.search_full())
# mmd = Request_Buy("300>","2","130","20000101")