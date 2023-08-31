import unittest
import pandas as pd

class MyFuncTestCase(unittest.TestCase):
    
    def test_convert_seconds_to_timedelta(self):
        df = pd.DataFrame({'time_UK': [0, 930233, 0, 783732, 0, 0]})
        
        # Sets the 0 second values to NaT    
        df.loc[df['time_UK'] == 0.0, 'time_UK'] = pd.NaT
        
        # Converts seconds to TimeDelta type
        df['time_UK'] = pd.to_timedelta(df['time_UK'], unit='s')
        
        self.assertEqual(df['time_UK'].tolist(), [pd.NaT, pd.to_timedelta(930233, unit='s'), pd.NaT, pd.to_timedelta(783732, unit='s'), pd.NaT, pd.NaT])
    

unittest.main()