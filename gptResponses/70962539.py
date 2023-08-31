# In order to extract the top 5 expensive services by checking the sum of cost for each date, you can modify your code as follows:

# ```
import random
import pandas as pd
import matplotlib.pyplot as plt

dates = ["2022-02-13T13:43:22+00:00", "2022-02-14T13:43:22+00:001", "2022-02-15T13:43:22+00:00", "2022-02-16T13:43:22+00:00"]

service_name = ["Example service 1", "Example service 2", "Example service 3", "Example service 4", "Example service 5", "Example service 6", "Example service 7", "Example service 8", "Example service 9", 'Example 10']
data = []
for i in range(0,50):
    tmp_data = {
        "usage_start_date": random.choice(dates),
        "cost": random.randrange(100),
        "service_name": random.choice(service_name)
        }
    data.append(tmp_data)
df = pd.DataFrame(data)
df['usage_start_date'] = pd.to_datetime(df['usage_start_date'], utc=True).dt.tz_convert(None).dt.date

df['usage_start_date'] = pd.to_datetime(df['usage_start_date'], format='%Y-%m-%d')
grouped_data = df.groupby(['usage_start_date', 'service_name'], as_index=False, group_keys=True).sum()

# Select the top 5 expensive services for each date
top5_expensive = grouped_data.groupby('usage_start_date').apply(lambda x: x.nlargest(5, 'cost')).reset_index(drop=True)

top5_pivot = top5_expensive.pivot(index="usage_start_date", columns="service_name", values="cost")

top5_pivot.plot(kind="bar", stacked=True, width=0.2)
plt.legend(title="Service names")
plt.show()
# ```

# In the code above, `grouped_data.groupby('usage_start_date').apply(lambda x: x.nlargest(5, 'cost')).reset_index(drop=True)` selects the top 5 expensive services for each date using the `nlargest()` function. Then, `top5_pivot = top5_expensive.pivot(index="usage_start_date", columns="service_name", values="cost")` creates a pivot table with the top 5 expensive services for each date. Finally, you can plot the stacked bar graph using the `plot()` function.