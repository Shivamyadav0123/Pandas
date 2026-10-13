# import pandas as pd
# s=pd.Series([10,20,30,40,50,60])
# print(s)

# import pandas as pd
# s=pd.Series([10,20,30,40])
# print(s)


# import pandas as pd
# Data={
#     "name":["Ram","Shyam","Shivam","Anshul"],
#     "Age":[20,30,40,50],
#     "Marks":[89,98,96,84]
# }
# s=pd.DataFrame(Data)
# print(s)
# print(s.shape)
# print(s.size)
# print(s.ndim)
# print(s.columns)
# print(s.index)
# print(s.dtypes)


#Data ko dekhane ke method 
# import pandas as pd
# Data={
#     "name":["Ram","Shyam","Shivam","Anshul"],
#     "Age":[20,30,40,50],
#     "Marks":[89,98,96,84]
# }
# s=pd.DataFrame(Data)
# print(s)
# print(s.head())

# import pandas as pd
# Data={
#     "name":["Ram","Shyam","Shivam","Anshul"],
#     "Age":[20,30,40,50],
#     "Marks":[89,98,96,84]
# }
# s=pd.DataFrame(Data)
# print(s.tail(2))

# import pandas as pd
# s=pd.Series([10,20,30,40,50,60])
# print(s)

# import pandas as pd
# Data={
#     "name":["Ram","Shyam","Shivam","Anshul"],
#     "Age":[20,30,40,50],
#     "Marks":[89,98,96,84]
# }
# s=pd.DataFrame(Data)
# print(s.info())

# import pandas as pd
# Data={
#     "name":["Ram","Shyam","Shivam","Anshul"],
#     "Age":[20,30,40,50],
#     "Marks":[89,98,96,84]
# }
# s=pd.DataFrame(Data)
# print(s.describe())

#Data read karna
#read_csv()
#s=pd.read_csv("student.csv")

#read_excel()
#s=pd.read_excel("studend.xlsx")

#read_json()
#s=pd.read_json("student.json")

#Data frame save and write karna
#to_csv()
#s=to_csv("output.csv",index=False)
#index false ka mutlab index save nhi hoga

# to_excel()
# s=to_excel("output.xlsx",index=False)

#to_json()
#s=to_json("output.json",index=False)

#colum selact karna
#print(s["name"])

#multilpe colum
#print(s[["name","marks"]])

# import pandas as pd
# Data={
#     "name":["Ram","Shyam","Shivam","Anshul"],
#     "Age":[20,30,40,50],
#     "Marks":[89,98,96,84]
# }
# s=pd.DataFrame(Data)
# print(s["name"])

# import pandas as pd
# Data={
#     "name":["Ram","Shyam","Shivam","Anshul"],
#     "Age":[20,30,40,50],
#     "Marks":[89,98,96,84]
# }
# s=pd.DataFrame(Data)
# print(s[["name","Marks"]])

# import pandas as pd
# Data={
#     "name":["Ram","Shyam","Shivam","Anshul"],
#     "Age":[20,30,40,50],
#     "Marks":[89,98,96,84]
# }
# s=pd.DataFrame(Data)
# print(s.loc[0])

# import pandas as pd
# Data={
#     "name":["Ram","Shyam","Shivam","Anshul"],
#     "Age":[20,30,40,50],
#     "Marks":[89,98,96,84]
# }
# s=pd.DataFrame(Data)
# print(s.loc[0:1,["name","Marks"]])

# import pandas as pd
# Data={
#     "name":["Ram","Shyam","Shivam","Anshul"],
#     "Age":[20,30,40,50],
#     "Marks":[89,98,96,84]
# }
# s=pd.DataFrame(Data)
# print(s.loc[s["Marks"]>90])

#position index number ke according data select karta hai
# import pandas as pd
# Data={
#     "name":["Ram","Shyam","Shivam","Anshul"],
#     "Age":[20,30,40,50],
#     "Marks":[89,98,96,84]
# }
# s=pd.DataFrame(Data)
# print(s.iloc[0,2])

#column add karna
# import pandas as pd
# Data={
#     "name":["Ram","Shyam","Shivam","Anshul"],
#     "Age":[20,30,40,50],
#     "Marks":[89,98,96,84]
# }
# s=pd.DataFrame(Data)
# p=s["City"]=["Lucknow","kanpur","Hardoi","Delhi"]
# print(s)

#column delete karna
# import pandas as pd
# Data={
#     "name":["Ram","Shyam","Shivam","Anshul"],
#     "Age":[20,30,40,50],
#     "Marks":[89,98,96,84]
# }
# s=pd.DataFrame(Data)
# p=s.drop("City",axis=1,inplace=True)
# print(s)

#inplace=true ka matlab original dataframe me change hoga

#Sorting
#Sort_value()
# import pandas as pd
# Data={
#     "name":["Ram","Shyam","Shivam","Anshul"],
#     "Age":[20,30,40,50],
#     "Marks":[89,94,96,85]
# }
# s=pd.DataFrame(Data)
# p=s.sort_values("Marks")
# print(p)

# import pandas as pd
# da=pd.read_excel("data.xlsx")
# print(da)

# import pandas as pd
# da=pd.read_excel("data.xlsx")
# b=pd.isna(da)
# print(b)

# import pandas as pd
# da=pd.read_excel("data.xlsx")
# p=da.fillna(0)
# print(p)

# import pandas as pd
# da=pd.read_excel("data.xlsx")
# p=da.isna().sum()
# print(p)

# import pandas as pd
# da=pd.read_excel("data.xlsx")
# p=da.dropna(axis=0)
# print(p)

# import pandas as pd
# da=pd.read_excel("data.xlsx")
# p=da.drop(["Placement_Eligible"],axis=1)
# print(p)

import pandas as pd
lst=[10,20,30,40]
ba=["A","B","C","D"]
a=pd.Series(lst,index=ba)
print(a)
