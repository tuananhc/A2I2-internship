# To create the desired outcome, you can use a dictionary to store the sum of items for each category. Here's one way to do it:

# ```python
given_list = [
    {"cat_id": 1, "category": "red", "items": 1},
    {"cat_id": 1, "category": "red", "items": 3},
    {"cat_id": 2, "category": "yellow", "items": 2},
    {"cat_id": 2, "category": "yellow", "items": 4},
    {"cat_id": 2, "category": "yellow", "items": 6},
    {"cat_id": 3, "category": "green", "items": 99},
]

category_sums = {}
for item in given_list:
    cat_id = item['cat_id']
    category = item['category']
    items = item['items']
    if cat_id in category_sums:
        category_sums[cat_id]['items'] += items
    else:
        category_sums[cat_id] = {'cat_id': cat_id, 'category': category, 'items': items}

outcome = list(category_sums.values())
print(outcome)
# ```

# Output:
# ```
# [
#     {'cat_id': 1, 'category': 'red', 'items': 4},
#     {'cat_id': 2, 'category': 'yellow', 'items': 12},
#     {'cat_id': 3, 'category': 'green', 'items': 99}
# ]
# ```

# In this solution, a dictionary named `category_sums` is used to store the sum of items for each category. The code iterates over each item in the given list and updates the sums in `category_sums`. If a category is encountered for the first time, a new dictionary is created and added to `category_sums`. Finally, the list of dictionaries is extracted from `category_sums` to get the desired outcome.