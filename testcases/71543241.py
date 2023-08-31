import unittest

def myFunc(data):
    years = {}
    counts = {}
    
    for item in data:
        year = item[1]
        value = float(item[5])
        
        if year in years:
            years[year] += value
            counts[year] += 1
        else:
            years[year] = value
            counts[year] = 1
    
    averages = []
    
    for year in years:
        average = years[year] / counts[year]
        averages.append([int(year), average])
    
    return averages

class MyFuncTestCase(unittest.TestCase):
    def test_myFunc(self):
        data = [
            ['425842', '2008', 'Monday', '23:30:00', '10'],
            ['425843', '2008', 'Tuesday', '23:30:00', '9'],
            ['425844', '2009', 'Monday', '23:30:00', '2'],
            ['425845', '2009', 'Monday', '23:30:00', '3'],
            ['425846', '2010', 'Monday', '23:30:00', '2'],
            ['425847', '2010', 'Monday', '23:30:00', '10'],
            ['425848', '2010', 'Tuesday', '23:30:00', '10']
        ]
        
        result = myFunc(data)
        
        self.assertEqual(result, [[2008, 9.5], [2009, 2.5], [2010, 7.3]])

unittest.main()