```python
import pandas as pd
import matplotlib.pyplot as plt
import random
import unittest

class TestMyFunc(unittest.TestCase):
    
    def test_nlargest_services(self):
        dates = ["2022-02-13T13:43:22+00:00", "2022-02-14T13:43:22+00:001", "2022-02-15T13:43:22+00:00", "2022-02-16T13:43:22+00:00"]
        service_name = ["Example service 1", "Example service 2", "Example service 3", "Example service 4",
                        "Example service 5", "Example service 6", "Example service 7", "Example service 8",
                        "Example service 9", 'Example 10']
        data = []
        for i in range(0, 50):
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
        df1 = grouped_data.sort_values(by=['usage_start_date', 'cost'], ascending=[False, False])
        
        result = df1.groupby('usage_start_date').head(5)
        top_5_services = result.pivot(index="usage_start_date", columns="service_name", values="cost")
        
        self.assertEqual(len(top_5_services.columns), 5)
        self.assertTrue(len(top_5_services) <= 5)
```