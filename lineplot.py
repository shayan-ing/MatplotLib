import matplotlib.pyplot as plt

x = ["day1","day2","day3","day4","day5"]
y = [300,420,250,230,400]
y1 = [350,450,200,300,100]

plt.plot(x , y, marker="o", ls = "--", color = "red", label= "week1")
plt.plot(x , y1, marker="*", ls = "-", color = "green", label = "week2", alpha = 0.5) #marker puts marker in graph points
# ls puts -- type lining in our drawed graph
# color changes the color of line graph
# alpha is used to reduce opacity
plt.legend()
plt.show()
     