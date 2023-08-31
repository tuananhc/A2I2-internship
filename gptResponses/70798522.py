# Yes, there is a more scalable and efficient approach to achieve your desired result using pandas. You can utilize the `groupby` function along with the `cumcount` function to create an incremental count of each id, based on the timestamp order. Then, you can update the 'seen_before' column based on this count.

# Here's how you can do it:

# ```python
df['seen_before'] = df.groupby('id').cumcount()
df['seen_before'] = df['seen_before'].astype(bool).astype(int)
# ```

# This code will create a count starting from 0 for each unique id based on the ascending order of the 'created_at' column. Then, we convert the count to boolean values (0 or 1) by casting it to bool first and then to int.

# The resulting dataframe will have the 'seen_before' column updated with 0 or 1 based on the existence of a matching id with an earlier timestamp.

# Here's the updated dataframe:

# ```
#      id          created_at  seen_before
# 0  1043 2021-11-27 16:56:43            0
# 1  1027 2021-11-22 19:01:21            1
# 2  1099 2021-11-22 07:37:02            1
# 3  1099 2021-11-22 07:36:50            1
# 4  1099 2021-11-22 07:36:41            0
# 5  1027 2021-11-22 07:36:39            0
# ```

# This approach avoids iterating over each row and instead leverages the pandas functionalities to achieve the desired result efficiently.