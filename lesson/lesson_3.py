import matplotlib.pyplot as plt


x_value = list(range(1, 5001))
y_value = [x**3 for x in x_value]

#plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Blues, edgecolor='none', s=40)
plt.scatter(x_value, y_value, c=(0, 0.7, 0.1),  edgecolor='none', s=40)

plt.title("Suare Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.axis([0, 5000, 0, 150000000000])

plt.savefig('../img/squares_plot3.png', bbox_inches='tight')
plt.show()