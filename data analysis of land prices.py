import numpy as np

import pandas as pd




"""
Question 1.

What is the state with the cheapest land?
what year was the cheapest?
where is the most expensive land? When?
cheapest region?
Most Expensive?

question 2.

What is the trend for land price over time?
What type of land is the cheapest?
idaho land trend?
SD land trend?
wyoming land trend?
North Dakota Land trend?

"""

df = pd.read_csv("Combined_Clean.csv")



print("What is the state with the cheapest land? what year was the cheapest?")
print()




print(df.sort_values("Acre Value").head(5))




print()
print("What is the state with the most expensive land? what year was the most expensive?")
print()




print(df.sort_values("Acre Value", ascending = False, na_position ='last').head(5))




print()
print("What is the cheapest region and year?")
print()




regions = df["Region or State"] == "Region"
print(df[regions].sort_values("Acre Value").head(5))




print()
print("What is the most expensive region and year")
print()




print(df[regions].sort_values("Acre Value", ascending = False, na_position ='last').head(5))




print()
print("What is the trend for land price per year")
print()







print(df.groupby(["Year"])["Acre Value"].mean())




print()
print("What land type is the most expensive and which is cheapest")
print()




print(df.groupby(["LandCategory"])["Acre Value"].mean())





print()
print("What is South dakotas land price trend over time?")
print()



maskx = df["State"] == "South Dakota"
print(df[maskx].groupby(["Year"])["Acre Value"].mean())




print()
print("What is Idahos land price trend over time?")
print()





maskx = df["State"] == "Idaho"
print(df[maskx].groupby(["Year"])["Acre Value"].mean())




print()
print("What is Wyomings land price trend over time?")
print()


maskx = df["State"] == "Wyoming"
print(df[maskx].groupby(["Year"])["Acre Value"].mean())





print()
print("What is North Dakotas land price trend over time?")
print()



maskx = df["State"] == "North Dakota"
print(df[maskx].groupby(["Year"])["Acre Value"].mean())
