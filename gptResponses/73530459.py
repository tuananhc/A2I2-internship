# To plot the 2D arrays as scatter plot markers without saving them as PNG images, you can use the `imshow()` function from matplotlib. Here's an example of how you can do it:

# ```python
import matplotlib.pyplot as plt
import numpy as np

images = np.random.uniform(0, 1, (5, 10, 10))
x, y = np.array([0, 2, -3, 6, 6.5]), np.array([10, 3, -2, -1, 0.2])

fig, ax = plt.subplots()
for i in range(len(images)):
    ax.imshow(images[i], extent=(x[i] - 0.5, x[i] + 0.5, y[i] - 0.5, y[i] + 0.5), origin='lower')

ax.scatter(x, y, color='red')  # Optional: Add scatter plot markers

plt.show()
# ```

# This code uses the `imshow()` function to plot each image as a marker with a size of 1 in both x and y directions. The `extent` parameter specifies the x and y limits for each individual marker based on the given coordinates. The `origin='lower'` parameter sets the origin to the lower left corner of the image.

# After plotting the images as markers, you can also add scatter plot markers using the `scatter()` function if desired.