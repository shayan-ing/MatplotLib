import matplotlib.pyplot as plt
import pandas as pd
# brands = ["Oneplus", "Apple", "Samsung", "Nokia","Redmi"]

# x = [22,35,30,3,10]
# c = ["red","violet","green","blue","orange"]
# ex = [0.1,0,0,0,0]
# plt.pie(x, labels=brands,colors=c, explode=ex,shadow=True,autopct="%.2f",startangle=90)
# plt.show()

data = pd.read_excel("expense3.xlsx")
df = pd.DataFrame(data)
print(df)
grouped_by = df.groupby("Payment Mode")["Amount"].sum()
print(grouped_by)
plt.pie(grouped_by.values, labels = grouped_by.index, autopct= "%.2f")
plt.show()
print(df)