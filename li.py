# import pandas as pd
# a=pd.read_excel("data2.xlsx")
# b=pd.pivot_table(a,values="Department",index="Salary",columns="Name",aggfunc="mean")
# print(b)

# a=["Ram","Shyam","Shivam","Anshul"]
# print(list(map(str.upper, a)))

# import pandas as pd
# a=pd.read_excel("data2.xlsx")
# b=a.groupby("Department")["Salary"].mean()
# print(b)


# import pandas as pd
# a=pd.read_excel("data2.xlsx")
# a["Joining_Date"]=pd.to_datetime(a["Joining_Date"])
# print(a["Joining_Date"].dt.day_name())
# print(a["Joining_Date"].dt.month_name())
# print(a["Joining_Date"].dt.year)


# a=["Ram","Shyam","Shivam","Anshul"]
# print(list(filter(lambda x: x.startswith("S"), a)))

# import pandas as pd
# a=pd.read_excel("data.xlsx")
# b=a.fillna({"City":"unknoewn","Marks":98})
# print(b)

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
# a={
#     "Name":["Ram","Shyam","Shivam","Anshul"],
#     "City":["Delhi","Mumbai","Kolkata","Chennai"],
#     "Salary":[50000,60000,70000,80000],
#     "Department":["IT","HR","Finance","Marketing"]
# }
# index=["A","B","C","D"]
# b=pd.DataFrame(a,index=index)
# print(b.iloc[2])

import pandas as pd
a=pd.read_excel("data.xlsx")
print(a.iloc["Aditya","Nisha"]==a.loc["Aditya","Nisha"])