import pandas as pd
da=pd.read_excel("data2.xlsx")
da["Joining_Date"]=pd.to_datetime(da["Joining_Date"],format="%Y-%m-%d")
da["Joining_Date"]=da["Joining_Date"].dt.strftime("%d-%Y-%m")
print(da)