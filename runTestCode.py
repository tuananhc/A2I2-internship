import subprocess
import os
import pandas as pd
from tqdm import tqdm

parentDir = "Test Environment/resultS"
count = 0

data = []

for dir in os.listdir(parentDir):
    path = os.path.join(parentDir, dir)
    print(path)
    testResult = subprocess.run(["python3", path + "/tests.py"], capture_output=True, text=True)
    testResult = testResult.stderr[:2]
    data.append([dir] + list(testResult))

df = pd.DataFrame(data, columns=["ID","GPT", "SO"])
df.set_index("ID")
print(df.to_string(index=False))