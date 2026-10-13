# import pandas as pd
# da=pd.read_excel("data2.xlsx")
# da["Joining_Date"]=pd.to_datetime(da["Joining_Date"],format="%Y-%m-%d")
# da["Joining_Date"]=da["Joining_Date"].dt.strftime("%d-%Y-%m")
# print(da)

# import pandas as pd
# da=pd.read_excel("data2.xlsx")
# da["Joining_Date"]=pd.to_datetime(da["Joining_Date"])
# print(da["Joining_Date"].dt.day_name())
# print(da["Joining_Date"].dt.month_name())
# print(da["Joining_Date"].dt.year)

# import pandas as pd
# a=pd.read_excel("data2.xlsx")
# a["Joining_Date"]=pd.to_datetime(a["Joining_Date"])
# print(a["Joining_Date"].dt.day_name())
# print(a["Joining_Date"].dt.month_name())
# print(a["Joining_Date"].dt.year)

# import pandas as pd
# a=pd.read_excel("data2.xlsx")
# print(a[(a["Birth_Date"]>="2001-04-01") & (a["Birth_Date"]<="2002-04-01")])

# import pandas as pd
# print(pd.Timestamp.now())

# import pandas as pd
# print(pd.Timestamp.now().date())

# import pandas as pd
# print(pd.Timestamp.now().day_name())

# import pandas as pd
# print(pd.Timestamp.now().year)

# import pandas as pd
# a=pd.read_excel("data2.xlsx")
# b=(a["Joining_Date"].dtype)
# print(b)

# import pandas as pd
# a=pd.read_excel("data2.xlsx")
# b=a.groupby("Department")["Salary"].mean()
# print(b)

import pandas as pd
a=pd.read_excel("data2.xlsx")
b=pd.pivot_table(a,values="Department",index="Salary",columns="Name",ass="mean")
print(b)