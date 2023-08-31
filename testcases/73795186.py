import unittest
from ast import literal_eval

def myFunc(list_of_sequencies, input_seq):
    result = []
    for idx, lst in enumerate(list_of_sequencies):
        for tup in lst:
            if input_seq in tup[1]:
                result.append((idx+1, tup))
    return {'id': [t[0] for t in result], 'list_of_sequencies': [t[1] for t in result]}

class MyFuncTestCase(unittest.TestCase):
    def setUp(self):
        self.list_of_sequencies = [
            [(8, ['1-1']), (4, ['0-3', '1-1']), (2, ['0-4', '1-1']), (2, ['1-2']), (1, ['1-1', '0-3']), (1, ['1-1', '0-41']), (1, ['1-1', '0-42']), (1, ['1-1', '0-43']), (1, ['1-1', '0-44']), (1, ['1-1', '0-45'])],
            [(15, ['1-1']), (5, ['0-1', '1-1']), (4, ['0-2', '1-1']), (4, ['1-1', '1-1']), (3, ['0-4', '1-1']), (3, ['1-1', '0-4']), (3, ['1-1', '0-4', '1-1']), (3, ['1-1', '0-40']), (3, ['1-1', '0-46']), (3, ['1-3'])],
            [(16, ['1-1']), (7, ['1-2']), (4, ['0-1', '1-1']), (4, ['1-2', '0-46']), (3, ['1-1', '0-42']), (3, ['1-3']), (2, ['1-1', '0-40']), (2, ['1-1', '0-41']), (2, ['1-1', '0-47']), (2, ['1-1', '1-1'])],
            [(74, ['1-1']), (51, ['1-1', '0-47']), (23, ['1-2']), (18, ['1-2', '0-46']), (10, ['0-1', '1-1']), (9, ['0-1', '1-1', '0-46']), (9, ['1-1', '0-46']), (6, ['1-3']), (5, ['0-2', '1-1']), (5, ['1-1', '0-45'])],
            [(178, ['1-9']), (140, ['1-9', '0-39']), (102, ['1-10']), (87, ['1-10', '0-38']), (75, ['1-1']), (53, ['1-8']), (50, ['0-1', '1-1']), (35, ['1-8', '0-40']), (32, ['1-9', '1-1']), (30, ['1-1', '0-36'])]
        ]
    
    def test_search_sequence(self):
        input_seq = ['0-1', '1-1']
        expected_result = {'id': ['5', '4', '2', '3'], 'list_of_sequencies': [
            [('0-1', '1-1')],
            [('0-1', '1-1')],
            [('0-1', '1-1')],
            [('0-1', '1-1')]
        ]}
        result = myFunc(self.list_of_sequencies, input_seq)
        self.assertEqual(result, expected_result)
    
    def test_sequence_not_found(self):
        input_seq = ['1-10', '0-47']
        expected_result = {'id': [], 'list_of_sequencies': []}
        result = myFunc(self.list_of_sequencies, input_seq)
        self.assertEqual(result, expected_result)

unittest.main()