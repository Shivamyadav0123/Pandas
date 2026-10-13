# import pandas as pd
# a=pd.read_excel("pa.xlsx")
# print(a)

#3
# import pandas as pd
# a=pd.read_excel("pa.xlsx")
# a["Schlarship"]="Rejected "
# print(a)

#4
# import pandas as pd
# a=pd.read_excel("pa.xlsx")
# a.loc[a["Attendance"]>80, "scholarship_status"]="Verified"
# print(a)

#5
# import pandas as pd
# a=pd.read_excel("pa.xlsx")
# a["Store"]=a["Marks"]+5
# print(a)

# import pandas as pd
# a=pd.read_excel("pa.xlsx")
# print(a)
# b=a.loc[5:28,"Marks"]=a.loc[5:28,"Marks"]+5
# print(b)

# import pandas as pd
# a=pd.read_excel("dd.xlsx")
# b=a.groupby("Department")["Fees_Paid"].sum()
# print(b)

# import pandas as pd
# a=pd.read_excel("dd.xlsx")
# print(a)

# import pandas as pd
# a=pd.read_excel("dd.xlsx")
# b=a[a["Exam_Status"]=="Pass"].groupby("Department").size()
# print(b)

# import pandas as pd
# a=pd.read_excel("dd.xlsx")
# b=a.groupby(["Department","City"])["Student_ID"].count()
# print(b)

# import pandas as pd
# a=pd.read_excel("data.xlsx")
# b=a[a.duplicated("Age")]
# print(b)
# print(a)

#import pandas as pd
# a=pd.read_excel("data.xlsx")
# b=a[a("Age")]
# print(b)
# print(a)

#order by
# import pandas as pd
# da=pd.read_excel("data.xlsx")
# print(da["Name"].str.upper())

# import pandas as pd
# da=pd.read_excel("data.xlsx")
# print(da["Name"].str.lower())

# import pandas as pd
# da=pd.read_excel("data.xlsx")
# print(da["Name"].str.title())

# import pandas as pd
# da=pd.read_excel("data.xlsx")
# b=da["Name"].sort_values(ascending=True)
# print(b)

# import pandas as pd
# da=pd.read_excel("data.xlsx")
# print(da["Attendance"].sort_values(ascending=True,na_position="first"))

#Date and time

import pandas as pd
da=pd.read_excel("data2.xlsx")
da["Joining_Date"]=pd.to_datetime(da["Joining_Date"],format="%Y-%m-%d")
da["Joining_Date"]=da["Joining_Date"].dt.strftime("%d-%m-%Y")
print(da)