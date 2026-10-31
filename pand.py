# import pandas as pd
# a=pd.read_excel("data2.xlsx")
# print(a)
# b=a.isna().sum()
# print(b)
# c=a.pivot_table(values="Salary",index="City",columns="Department",aggfunc="mean").fillna(0)
# print(c)

# a=["Ram","Shyam","Shivam","Anshul"]
# print(list(map(str.upper, a)))

# a=["Ram","Shyam","Shivam","Anshul"]
# print(list(filter(lambda x: x.startswith("S"), a)))

# import functools as ft
# a=[1,2,3,4,5]
# print(ft.reduce(lambda x,y: x+y, a))

# import pandas as pd
# a=pd.Series([1,2,3,4,5],index=["A","B","C","D","E"])
# b=["A","B","C","D","E"]
# print(a)

# import pandas as pd
# a=pd.read_excel("data2.xlsx")
# a["Department"].map({"IT": "Information Technology", "HR": "Human Resources", "Finance": "Financial Department", "Marketing": "Marketing Department", "Sales": "Sales Department",})
# print(a)

import pandas as pd
a=pd.read_excel("data2.xlsx")
b=a.filter(items=["Department"])
print(a[b["Department"]=="IT"])