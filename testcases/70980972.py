import unittest
import pandas as pd
import numpy as np

def myFunc():
    present = 12
    died = 20

    dataSet = {'id': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'C'],
               'id_2': [1, 2, 3, 1, 1, 2, 3, 1],
               'start': [9, 13, 12, 11, 9, 20, 22, 13],
               'end': [14, 22, 21, 19, 10, 30, 24, 18]}

    df = pd.DataFrame(dataSet, columns=['id', 'id_2', 'start', 'end'])

    df_start = df.loc[(df['start'] <= present) & (df['end'] >= present)]
    df_between = df.loc[(df['start'] >= present) & (df['end'] <= died)]
    df_end = df.loc[(df['start'] <= died) & (df['end'] >= died)]

    df_combined = pd.concat([df_start, df_between, df_end]).drop_duplicates()

    return df_combined

class MyFuncTest(unittest.TestCase):

    def test_df_combined(self):
        df_combined = myFunc()
        expected_output = pd.DataFrame({
            'id': ['A', 'A', 'A', 'A', 'B', 'C'],
               'id_2': [1, 2, 3, 1, 2, 1],
               'start': [9, 13, 12, 11, 20, 13],
               'end': [14, 22, 21, 19, 30, 18]
        }, columns=['id', 'id_2', 'start', 'end'])

        self.assertTrue(df_combined.equals(expected_output))

unittest.main(argv=[''], verbosity=2, exit=False)