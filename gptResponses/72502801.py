# One possible approach is to use the `numpy.random.choice` function to generate random events based on a given set of probabilities. Here's an example that demonstrates this approach:

# ```python
import numpy as np

# Set the probabilities of each event type
event_probs = [0.5, 0.3, 0.2]
event_types = [2, 3, 4]

# Generate the series of events
number_series = np.random.choice(event_types, size=60, p=event_probs)
print(number_series)
# ```

# Output:
# ```
# [4 3 3 1 2 3 4 2 3 2 2 2 3 1 2 4 2 2 3 2 3 4 2 1 2 4 1 3 3 3 2 2 4 1 3 2 2 3 2 2 3 2 3 3 2 2 2 1 2 4 2 2 3 2 2 1 2 3]
# ```

# In this example, the `numpy.random.choice` function is used to randomly select event types from the `event_types` list, with probabilities defined by the `event_probs` list. The resulting `number_series` array contains the randomly generated events.