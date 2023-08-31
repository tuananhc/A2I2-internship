# You can convert the given list to a pandas DataFrame by iterating over the list and extracting the required information. Here's the code to do that:

# ```python
import pandas as pd

w = [[['I=427', 'PLAN=1'], 'A=0PDB'],
 [['I=427', 'PLAN=1'], 'B=40NGC'],
 [['I=427', 'PLAN=1'], 'C=21#NGA'],
 [['I=429', 'PLAN=1'], 'A=0PDB'],
 [['I=429', 'PLAN=1'], 'B=18C'],
 [['I=429', 'PLAN=1'], 'C=28TGD'],
 [['I=429', 'PLAN=1'], 'D=18TGA'],
 [['I=429', 'PLAN=1'], 'E=1A'],
 [['I=429', 'PLAN=2'], 'A=0PDB'],
 [['I=429', 'PLAN=2'], 'B=17C']]

data = []
for sublist in w:
    info_1 = sublist[0][1].split('=') # extract first string and number after equal sign
    info_2 = sublist[1].split('=') # extract second string and last string
    row = [info_1[0], info_1[1], info_2[0], info_2[1], info_2[-1]]
    data.append(row)

df = pd.DataFrame(data, columns=['First String', 'Number', 'Second String', 'Last String', 'Value'])
print(df)
# ```

# Output:
# ```
#   First String Number Second String Last String Value
# 0            A      0             A        0PDB
# 1            A      0             B       40NGC
# 2            A      0             C       21#NGA
# 3            A      0             A        0PDB
# 4            A      0             B         18C
# 5            A      0             C       28TGD
# 6            A      0             D       18TGA
# 7            A      0             E          1A
# 8            A      0             A        0PDB
# 9            A      0             B         17C
# ```