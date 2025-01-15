import matplotlib.pyplot as plt

days  = [1,2,3,4,5,6,7]

w1 = [,10,30,20,35,60,80]
w2 = [50,60,30,75,80,90,120]
w3 = [8,30,50,60,70,90,100]

plt.stackplot(days,w1,w2,w3, colors= [ "pink","hotpink","magenta"], labels= ["week1","week3","week3"])
plt.legend()
plt.show()
# import pandas as pd

# data = pd.read_csv("food_data.csv")
# df = pd.DataFrame(data)
# # print(df)
# grouped  = df.groupby("Category")["Calories","Protein","Fats"].agg("mean")
# print(grouped)