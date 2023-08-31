You can use the `applymap` method to apply the `list` function to each value in the DataFrame and then use `dropna` to remove the NaN values. Here's an example:

```python
x = df_chunk.groupby('id', dropna=True).applymap(lambda x: [x] if pd.notnull(x) else []).agg(sum)
print(x)
```

This will give you the desired result where lists are formed for each column and NaN values are removed.