Here are some example unit test cases similar to the unittest library for the given task:

```python
import unittest
import json
from unittest.mock import patch
from io import StringIO

class MyFuncTestCase(unittest.TestCase):

    def test_recreate_relgraph(self):
        # Assuming the given code is inside a function called myFunc
        # Test if relgraph is recreated with each iteration
        
        # Test case 1: If show_relations is True
        show_relations = True
        graph = {
            'entities': {
                '1': {'head': 'entity1'},
                '2': {'head': 'entity2'},
                '3': {'head': 'entity3'}
            },
            'relations': [
                {'subject': '1', 'relation': 'relation1', 'object': '2'},
                {'subject': '2', 'relation': 'relation2', 'object': '3'}
            ]
        }
        
        expected_result = [
            ['entity1', 'relation1', 'entity2'],
            ['entity2', 'relation2', 'entity3']
        ]
        
        # Patching the _print function for testing purposes
        with patch('builtins.print'):
            with patch('builtins.open', create=True) as mock_open:
                with patch('json.dump') as mock_dump:
                    with patch('sys.stdout', new=StringIO()) as fake_out:
                        myFunc(show_relations, graph)
                        
                        # Check if relgraph is recreated with each iteration
                        mock_dump.assert_called_once_with(expected_result, mock_open.return_value.__enter__.return_value)
        
        # Test case 2: If show_relations is False
        show_relations = False
        
        # Patching the _print function for testing purposes
        with patch('builtins.print'):
            with patch('builtins.open', create=True) as mock_open:
                with patch('json.dump') as mock_dump:
                    with patch('sys.stdout', new=StringIO()) as fake_out:
                        myFunc(show_relations, graph)
                        
                        # Check if relgraph is empty when show_relations is False
                        mock_dump.assert_not_called()
                        
    def test_dump_relgraph_to_json(self):
        # Assuming the given code is inside a function called myFunc
        # Test if relgraph is dumped into a json file
        
        show_relations = True
        graph = {
            'entities': {
                '1': {'head': 'entity1'},
                '2': {'head': 'entity2'},
                '3': {'head': 'entity3'}
            },
            'relations': [
                {'subject': '1', 'relation': 'relation1', 'object': '2'},
                {'subject': '2', 'relation': 'relation2', 'object': '3'}
            ]
        }
        
        # Patching the _print function for testing purposes
        with patch('builtins.print'):
            with patch('builtins.open', create=True) as mock_open:
                with patch('json.dump') as mock_dump:
                    with patch('sys.stdout', new=StringIO()) as fake_out:
                        myFunc(show_relations, graph)
                        
                        # Check if relgraph is dumped into a json file
                        mock_dump.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```

Note: The above test cases assume that the `_print` and `_func` functions are defined correctly. The `myFunc` function should be defined outside the test cases and imported for testing. The patching and asserting is done based on the given code snippet and assumption of function definitions.