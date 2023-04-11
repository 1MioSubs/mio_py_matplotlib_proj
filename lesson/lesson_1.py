import matplotlib.pyplot as plt


input_value = [1, 2, 3, 4, 5]
squ = [1, 4, 9, 16, 25]
plt.plot(input_value, squ, linewidth=5)
plt.title("Suare Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)

plt.savefig('../img/squares_plot1.png', bbox_inches='tight')
plt.show()