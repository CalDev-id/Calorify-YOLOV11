import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("qtagg")

# Data
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]

# Create a plot
plt.plot(x, y)

# Add labels and title
plt.xlabel("X-axis Label")
plt.ylabel("Y-axis Label")
plt.title("Line Chart Example")

# Display the plot
plt.show()
