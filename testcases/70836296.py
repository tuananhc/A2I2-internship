import unittest
import sqlite3

def myFunc():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur2 = con.cursor()
    cur3 = con.cursor()
    data = cur.execute('''SELECT * FROM table_1''')
    columns = []
    for column in data.description:
        columns.append(column[0])
    for columnx in columns:
        cur2.execute(f'''SELECT {columnx} FROM table_1''')
        content = cur2.fetchall()
        for word in content:
            word = str(word)
            word = word.strip("(),' ")
            if word != "None":
                cur3.execute(f'''INSERT INTO table_1_V2 (column1, column2) VALUES (?,?);''',(str(word),str(columnx)))
    con.commit()

def transform():
    con = sqlite3.connect('database.db')
    cur = con.cursor()
    cur2 = con.cursor()
    cur3 = con.cursor()
    data = cur.execute('''SELECT * FROM table_1''')
    columns = []
    for column in data.description:
        columns.append(column[0])
    for columnx in columns:
        cur2.execute(f'''SELECT {columnx} FROM table_1''')
        content = cur2.fetchall()
        for word in content:
            word = str(word)
            word = word.strip("(),' ")
            if word != "None":
               cur3.execute(f'''INSERT INTO table_1_V2 (column1, column2) VALUES (?,?);''',(str(word),str(columnx)))
    con.commit()

class MyTestCase(unittest.TestCase):
    def test_transform(self):
        myFunc()
        # Assert the resulting transformed table structure
        
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute('''SELECT * FROM table_1_V2''')
        transformed_data = cur.fetchall()
        
        self.assertEqual(len(transformed_data), 6) # Check if there are 6 rows in the transformed table
        
        expected_data = [('banana', 'fruits'), ('apple', 'fruits'), ('broccoli', 'vegetables'), ('barley', 'grains'), ('tomato', 'vegetables'), ('wheat', 'grains')]
        
        self.assertEqual(transformed_data, expected_data) # Check if the transformed data matches the expected data

if __name__ == '__main__':
    unittest.main()