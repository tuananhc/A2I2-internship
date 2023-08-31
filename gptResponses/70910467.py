# To remove the scientific notation from the y-axis in bqplot, you can use the `tick_format` property of the y-axis. Here's an example code snippet:

# ```python
from bqplot import pyplot as plt2
import datetime

x_values = []  # array of datetimes
y_values = []  # array of 10+ digit numbers
plt2.show()

fig = plt2.figure()
axes_options = {'y': {'tick_format': '0.2f'}}  # Set the tick_format for the y-axis
axes = plt2.axes(options=axes_options)
lines = plt2.plot(x_values, y_values)

def functionThatIsCalledRepeatedly(x_val, y_val):
    x_values.append(x_val)
    y_values.append(y_val)
    lines.y = y_values  # Update the y-values of the line plot

plt2.show()
# ```

# In this code, we create a separate `figure` object and pass the `axes_options` dictionary to the `plt2.axes` function to set the `tick_format` for the y-axis. Then, we update the `y` attribute of the `lines` object to update the y-values of the line plot.

# I hope this helps! Let me know if you have any further questions.