# To recreate the `relgraph` list with each iteration, you can move the `relgraph=[]` statement inside the list comprehension before appending the values. Here's an updated version of your code:

# ```python
if show_relations:
    _print('Relations:')

    entities = graph['entities']
    relations_data = [
        [
            (relgraph := []),  # create empty relgraph list for each iteration
            
            entities[rel['subject']]['head'].lower(),
            relgraph.append(entities[rel['subject']]['head'].lower()),
            
            rel['relation'].lower(),
            relgraph.append(rel['relation'].lower()),
            
            entities[rel['object']]['head'].lower(),
            relgraph.append(entities[rel['object']]['head'].lower()),
            
            _print(relgraph)
        ]
        for rel in graph['relations']
    ]
# ```

# Using the `:=` (walrus operator) in the list comprehension allows you to assign and store the empty `relgraph` list within the comprehension itself.

# As for dumping the lists into a JSON file, you can use the `json` module in Python. Here's an example:

# ```python
import json

# Assuming you have the relations_data list from your code
with open('output.json', 'w') as json_file:
    json.dump(relations_data, json_file)
# ```

# This code will write the `relations_data` list to the file named "output.json" in JSON format.