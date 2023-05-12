import matplotlib.pyplot as plt

# Add input values so the graph has the correct x-coordinates.
input_values = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# Plot in a certain style
# To see the styles available from Mattplotlib
# open terminal > python3 > import matplotlib.pyplot as plt
# plt.style.available
plt.style.use("dark_background")

fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)

# Set chart title and label axees.
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# Set size of tick labels.
ax.tick_params(axis="both", labelsize=14)

plt.show()
# the function plt.show() opens Matplotlib's viewr and displays the plot
