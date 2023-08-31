# Yes, you can write a function to create the tables for each question and use a for loop to iterate over the questions. Here's an example:

# ```python
import pandas as pd

def create_tables(df, questions):
    tables = []

    for question in questions:
        out = df.pivot_table(index=question, columns=['Gender'], values=['ID'], aggfunc='count', fill_value=0)
        out = (out.join(out[['ID']].div(out['ID'].sum(axis=1).values, axis=0)
                    .mul(100)
                    .rename(columns={'ID':'%Respondents'})))
        tables.append(out)

    return tables

# Example usage
df = pd.DataFrame({
    'ID': ['001', '002', '003', '004', '005'],
    'Q1': ['Y', 'N', 'Y', 'Y', 'Y'],
    'Q2': ['N', 'Y', 'N', 'N', 'N'],
    'Q3': ['Y', 'Y', 'N', 'Y', 'Y'],
    'Gender': ['F', 'M', 'F', 'M', 'M'],
    'Age': [22, 35, 20, 54, 42],
    'Dept': ['IT', 'HR', 'IT', 'OPRE', 'OPRE']
})

questions = ['Q1', 'Q2', 'Q3']

tables = create_tables(df, questions)

for table in tables:
    print(table)
    print()
# ```

# This will create separate tables for each question and print them in the desired format. You can modify the function and the example code according to your specific requirements.