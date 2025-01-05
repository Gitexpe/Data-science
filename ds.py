import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

dataframe=pd.read_csv("C:\\Users\\gaura\\Documents\\python\\zomato_data.csv")
# print(dataframe.head())
# printing the first 5 rows of the dataframe.

# now refining data in the dataframe.
def handling_rate(rate):
    rate=rate.replace("/5","")
    return rate
dataframe["rate"]=dataframe["rate"].apply(handling_rate)
# print(dataframe["rate"].head())

# checking for null values in the dataframe.
# dataframe.info()


sns.countplot(x=dataframe["listed_in(type)"],palette="viridis")
# to get a bar graph of the count of the type of restaurant.
plt.xlabel("Type of restaurant")
plt.show(block=True)
plt.close()

# result : Most of the listed restaurants of zomato are Dining type.

grouped_data=dataframe.groupby("listed_in(type)")["votes"].sum()
result=pd.DataFrame({"votes":grouped_data})
plt.plot(result,c="red",marker="o")
plt.xlabel("Type of restaurant")
plt.ylabel("Votes")
plt.title("Votes of different type of restaurants")
plt.show(block=True)
plt.close()
# result : The votes of the Delivery type restaurants are the highest.

plt.hist(dataframe["rate"],bins=15)
plt.title("rate distribution")
plt.show(block=True)
plt.close()

