import matplotlib.pyplot as plt

x = [10,40,20,40,30,60,70,50,40]
plt.stem(x, linefmt = "--", markerfmt = "D", orientation='vertical')
plt.show()