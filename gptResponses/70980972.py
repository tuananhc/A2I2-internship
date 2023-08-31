# You can achieve the desired output by using boolean indexing with multiple conditions. Here's a simplified approach:

# 1. Create boolean masks for the three conditions:
#    - df_begin: ((df['start'] <= present) & (df['end'] >= present))
#    - df_between: ((df['start'] >= present) & (df['end'] <= died))
#    - df_end: ((df['start'] <= died) & (df['end'] >= died))

# 2. Combine the masks using the logical OR operator (|) to get a single mask:

#    <pre><code>mask = df_begin | df_between | df_end</code></pre>

# 3. Filter the DataFrame using the mask:

#    <pre><code>df_filtered = df[mask]</code></pre>

# This approach will give you the desired output while also being efficient for large datasets.

import pandas as pd
import numpy as np
# Create data set.
present = 12
died  = 20
dataSet = {'id': ['A', 'A', 'A','A','B','B','B','C'],
           'id_2': [1, 2, 3, 1, 1,2,3,1],
           'start' : [9,13,12,11,9,20,22,13],
           'end' : [14,22,21,19,10,30,24,18]}

# Create dataframe with data set and named columns.
df = pd.DataFrame(dataSet, columns= ['id', 'id_2', 'start','end'])

df_begin = ((df['start'] <= present) & (df['end'] >= present))
df_between = ((df['start'] >= present) & (df['end'] <= died))
df_end = ((df['start'] <= died) & (df['end'] >= died))

mask = df_begin | df_between | df_end

df_filtered = df[mask]

print(df_filtered)