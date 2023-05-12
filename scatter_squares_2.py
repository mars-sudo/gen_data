import matplotlib.pyplot as plt

# Add input values so the graph has the correct x-coordinates.
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

plt.style.use("dark_background")

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
# To plot a series of points, we can pass scatter() separate lists of x- and y- values.
x_values = [1, 2, 3, 4, 5]
y_values = [1, 4, 6, 8, 10]
ax.scatter(x_values, y_values, s=100)

# Set chart title and label axees.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis="both", which="major", labelsize=14)

plt.show()
# the function plt.show() opens Matplotlib's viewr and displays the plot
