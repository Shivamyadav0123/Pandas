# import pandas as pd 
# a=pd.read_excel("data.xlsx")
# b=a[a[["City", "Fees_Paid"]].isna().sum(axis=1) > 0]
# print(b)


# import pandas as pd 
# a=pd.read_excel("data.xlsx")
# b=a.loc[(a["City"]=="Varanasai") & (a["Department"]=="CSE")]
# print(b)

# import pandas as pd 
# a=pd.read_excel("data.xlsx")
# b=a.loc[a[[13,"City"]]]
# print(b)

# import pandas as pd 
# a=pd.read_excel("data.xlsx")
# b=a.loc[23,"City"]="landan"
# print(a)
# a.to_excel("data.xlsx",index=False)

# import pandas as pd
# a=pd.read_excel("data.xlsx")
# b=a.iloc[23:24,4]=a.iloc[23:24,4].fillna("america")
# print(a)

# import pandas as pd
# a=pd.read_excel("data.xlsx")

# import pandas as pd
# a=pd.read_excel("data.xlsx")
# print(a)

# import pandas as pd
# a=pd.read_excel("data.xlsx")
# b=a[a["City"].isnull()]
# print(b)

# import pandas as pd
# a=pd.read_excel("data.xlsx")
# b=a[a["Marks"].isnull()]
# print(b)

# import pandas as pd
# a=pd.read_excel("data.xlsx")
# b=a.dropna(subset=["City"])
# print(b)

# import pandas as pd
# a=pd.read_excel("data.xlsx")
# b=a.dropna(subset=["City","Marks"])
# print(b)

# import pandas as pd
# a=pd.read_excel("data.xlsx")
# b=a["City"]=a["City"].fillna("unknow")
# print(b)

# import pandas as pd
# a=pd.read_excel("data.xlsx")
# b=a.fillna({"City":"unknoewn","Marks":98})
# print(b)


# import pandas as pd
# a=pd.read_excel("data.xlsx")
# a["percentage"]=(a["Marks"]/100)*100
# print(a)

# import pandas as pd
# a=pd.read_excel("data.xlsx")
# a["scholar_status"]="Rejected"
# b=a.loc[a["Attendance"]>80,"scholar_status"]="Verified"
# print(b)
# print(a)

# import pandas as pd
# a=pd.read_excel("data.xlsx")
# b=a.drop(["Name"],axis=1,inplace=True)
# print(b)
# print(a)

# import pandas as pd
# a=pd.read_excel("data.xlsx")
# b=a.pop("City")
# print(b)
# print(a)

# import pandas as pd
# a=pd.read_excel("data.xlsx")
# a.loc[len(a)]=[1001,  "Rahul" ,"Male",  18.0 ,"" ,"CSE", "B.Tech" ,1,  62.0 ,45.0, 35000.0, "Pass" ,"Yes"]
# print(a)

# import pandas as pd
# a=pd.read_excel("data.xlsx")
# a.loc[len(a)]=[1002, "Amit", "Female"  19.0, "" ,"Delhi", "IT", "BCA", 2, 68.0, 52.0 ,40000.0, "Pass", "No"]
# print(a)

import pandas as pd
a=pd.read_excel("data.xlsx")
b=a.drop(a[a["Age"]<20].index)
print(b)