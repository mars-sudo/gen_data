import matplotlib.pyplot as plt

# Add input values so the graph has the correct x-coordinates.
# input_values = [1, 2, 3, 4, 5]
# squares = [1, 4, 9, 16, 25]

plt.style.use("seaborn")

fig, ax = plt.subplots()
# ax.plot(input_values, squares, linewidth=3)
# To plot a series of points, we can pass scatter() separate lists of x- and y- values.
x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

# To change the color of the points, pass c to scatter()
##### ax.scatter(x_values, y_values, c="red", s=10)

# Custom RGB tuple, decimal values bettween 0 and 1
#### ax.scatter(x_values, y_values, c=(0.1, 0.2, 0.3), s=10)

# A colormap is a series of colors in a gradient that moves from a starting to an ending color.
# Use colormaps in visualizaitions to emphasize a pattern in the data.
# For example, you might make low values a light colow and high values a darker color.
# To use one of the colormaps, you need to specify how pyplott should assign a color to each point
# in the data set.
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)


# Set chart title and label axees.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis="both", which="major", labelsize=14)

# Set the range for each axis
# The axis() method requires four values: the min and max values for x-axis and y-axis.
# Here we run the x-axiss from 0 to 1100 and the y-axis from 0 to 1,100,000
ax.axis([0, 1100, 0, 110000])

plt.show()
# the function plt.show() opens Matplotlib's viewr and displays the plot

# plt.savefig("squares_plot.png", bbox_inches="tight")
# To save the plot to a file, use the above line
# The first argument is a filename for the plot image, which will be saved
# in the working directory. The second arguement trims the extra whitespace from the plot.
