import pandas as pd
a=pd.read_excel("data2.xlsx")
print(a)

import pandas as pd
a=pd.read_excel("data2.xlsx")
print(a[["Name","Department"]])

import pandas as pd
a=pd.read_excel("data2.xlsx")
a["Total"]="Tatal"
print(a)

import pandas as pd
a=pd.read_excel("data2.xlsx")
print(a.drop("Tatal",axis=1))
