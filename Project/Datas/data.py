import pandas as pd
import os
#https://pandas.pydata.org/docs/reference/index.html

if os.path.exists("DataBase.csv"):
    pass
else:
    f = open("DataBase.csv","x")
    f.close()
os.chdir("Datas")

datas = pd.read_csv("DataBase.csv",delimiter=",")
# datas = datas.drop(0,1) # Droping Row
df2 = ["Salam","Salami"]
# datas.loc[len(datas)] = df2 # Add New Row
# datas.to_csv("DataBase.csv",index=False) # Last Line To Apply Changes
datas.iloc[-1] # Last Row Data
print(datas.iloc[-1])
