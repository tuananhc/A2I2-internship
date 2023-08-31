import unittest
import random

def myFunc(n):
    num_events = random.randint(1, 10)
    number_series = [1]*n
    first_pos = 0 
    event_starts = sorted([first_pos + i for i in random.sample(range(n), num_events)])
    event_ends = [sum(i) for i in list(zip(event_starts, random.sample(range(8), num_events)))]
    for c in list(zip(event_starts, event_ends)):
        rand_event_type  = random.choices(population=[2, 3, 4], weights=[0.5, 0.3, 0.2])[0]
        number_series[c[0]:c[1]] = [rand_event_type]*len(number_series[c[0]:c[1]])
    return number_series

class TestMyFunc(unittest.TestCase):
    
    def test_output_length(self):
        result = myFunc(60)
        self.assertEqual(len(result), 60)
    
    def test_output_values(self):
        result = myFunc(60)
        self.assertTrue(all(val in [1, 2, 3, 4] for val in result))
    
    def test_number_of_events(self):
        result = myFunc(60)
        num_events = result.count(2) + result.count(3) + result.count(4)
        self.assertLessEqual(num_events, 10)
    
    def test_event_types(self):
        result = myFunc(60)
        event_types = set(result) - set([1])
        self.assertSetEqual(event_types, {2, 3, 4})
    
    def test_event_probabilities(self):
        result = myFunc(60)
        num_events = result.count(2) + result.count(3) + result.count(4)
        prob_2 = result.count(2) / num_events if num_events != 0 else 0
        prob_3 = result.count(3) / num_events if num_events != 0 else 0
        prob_4 = result.count(4) / num_events if num_events != 0 else 0
        self.assertAlmostEqual(prob_2, 0.5, places=1)
        self.assertAlmostEqual(prob_3, 0.3, places=1)
        self.assertAlmostEqual(prob_4, 0.2, places=1)
        
unittest.main(argv=[''], verbosity=2, exit=False)