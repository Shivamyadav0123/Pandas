# import pandas as pd
# da=pd.read_excel("data2.xlsx") 
# print(da) 
# print(da[(da["Joining_Date"]>="2024-04-01") & (da["Joining_Date"]<="2025-04-01")])


import pandas as pd
a=pd.read_excel("data2.xlsx")
print(a)
b=a.isna().sum()
print(b)
c=a.pivot_table(values="Salary",index="City",columns="Department",aggfunc="mean")
print(c)

