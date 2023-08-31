import unittest
import pandas as pd

class MyTestCase(unittest.TestCase):
    
    def test_append_values_to_dataframe(self):
        empty_df = pd.DataFrame(columns=["date","builders","miners","roofers"])

        text = "On 10 May 2022, there were 400 builders living in Rome, there were also no miners and approximately 70 roofers"
        text = text.split()
        profession = ["builders","miners","roofers"]

        for i in text:
            if i in profession:
                empty_df = empty_df.append({"builders": text[text.index(i) - 1], "date": "10 May 2022"}, ignore_index=True)

        self.assertEqual(len(empty_df), 1)
        self.assertEqual(empty_df.at[0, "builders"], "400")
        # Add assertions for other columns

    def test_convert_none_to_zero(self):
        empty_df = pd.DataFrame(columns=["date","builders","miners","roofers"])

        text = "On 10 May 2022, there were 400 builders living in Rome, there were also no miners and approximately 70 roofers"
        text = text.split()
        profession = ["builders","miners","roofers"]

        for i in text:
            if i in profession:
                value = text[text.index(i) - 1]
                if value.lower() == "no" or value.lower() == "none":
                    value = 0
                empty_df = empty_df.append({"builders": value, "date": "10 May 2022"}, ignore_index=True)

        self.assertEqual(len(empty_df), 1)
        self.assertEqual(empty_df.at[0, "miners"], 0)
        # Add assertions for other columns

    def test_incorporate_date(self):
        empty_df = pd.DataFrame(columns=["date","builders","miners","roofers"])

        text = "On 10 May 2022, there were 400 builders living in Rome, there were also no miners and approximately 70 roofers"
        text = text.split()
        profession = ["builders","miners","roofers"]
        date = "10 May 2022"

        for i in text:
            if i in profession:
                value = text[text.index(i) - 1]
                if value.lower() == "no" or value.lower() == "none":
                    value = 0
                empty_df = empty_df.append({"builders": value, "date": date}, ignore_index=True)

        self.assertEqual(len(empty_df), 1)
        self.assertEqual(empty_df.at[0, "date"], "10 May 2022")
        # Add assertions for other columns

if __name__ == '__main__':
    unittest.main()