import matplotlib.pyplot as plt


x_value = [1, 2, 3, 4, 5]
y_value = [1, 4, 9, 16, 25]
plt.scatter(x_value, y_value, s=200)

plt.title("Suare Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)

plt.savefig('../img/squares_plot2.png', bbox_inches='tight')
plt.show()