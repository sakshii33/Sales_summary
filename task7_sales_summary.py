import sqlite3

# Connect or create the SQLite database
conn = sqlite3.connect('sales_data.db')
cursor = conn.cursor()

# Create the sales table
cursor.execute('''
CREATE TABLE IF NOT EXISTS sales (
    id INTEGER PRIMARY KEY,
    product TEXT,
    quantity INTEGER,
    price REAL
)
''')

# Insert sample data
sample_data = [
    ('Apples', 10, 2.5),
    ('Bananas', 5, 1.2),
    ('Apples', 7, 2.5),
    ('Oranges', 8, 3.0),
    ('Bananas', 10, 1.2)
]

cursor.executemany('INSERT INTO sales (product, quantity, price) VALUES (?, ?, ?)', sample_data)
conn.commit()
conn.close()
