import pandas as pd
import mysql.connector

# Read CSV
df = pd.read_csv('products.csv')

# Connect to local MariaDB/MySQL
conn = mysql.connector.connect(
    host='localhost',
    user='janani',
    password='Janani123!',
    database='ecommerce'
)

cursor = conn.cursor()

# Insert data
for _, row in df.iterrows():
    cursor.execute(
        "INSERT INTO products (name, category, price, stock) VALUES (%s, %s, %s, %s)",
        (row['name'], row['category'], row['price'], row['stock'])
    )

conn.commit()
print("✅ Data uploaded successfully!")

cursor.close()
conn.close()
