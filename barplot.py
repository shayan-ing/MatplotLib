import matplotlib.pyplot as plt

y = [98,67,88,95,88]

x = ["p1","p2","p3","p4","p5"]
colors = ["Red", "green","blue","orange","pink"]
plt.bar(x , y, color = colors, edgecolor= "black") 
plt.xlabel("Parts Of Harry Potter", fontsize = 17)
plt.ylabel("Popularity", fontsize = 17)
plt.title("Pop Of Diff Harrt Pot. Mov Series", fontsize =20)
plt.show()


# import matplotlib.pyplot as plt
# import numpy as np

# xpoints = np.array([0, 6])
# ypoints = np.array([0, 250])

# plt.plot(xpoints, ypoints)
# plt.show()