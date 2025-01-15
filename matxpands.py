import pandas as pd

import matplotlib.pyplot as plt

data = pd.read_excel("expense3.xlsx")

df = pd.DataFrame(data)
print(df)
# plt.bar(df["Payment Mode"],df["Amount"])
# plt.show()