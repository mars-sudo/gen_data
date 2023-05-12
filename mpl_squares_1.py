import matplotlib.pyplot as plt

# The pyplot module contains a number of functions that generate charts and plots.


squares = [1, 4, 9, 16, 25]
# A list of numbers called squares.

fig, ax = plt.subplots()
# variable fig represents the entire figure or collectionof plots that are generated.
# variable ax represents a single plot pin the figure.
# call the subplots() function to generate one or more plotes in the same figure.

ax.plot(squares)
# the plot() method will try to plot the data it's given in a meaningful way.

plt.show()
# the function plt.show() opens Matplotlib's viewr and displays the plot
