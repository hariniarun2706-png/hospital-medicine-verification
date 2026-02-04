import sqlite3

conn = sqlite3.connect("hospital.db")
cur = conn.cursor()

cur.execute("SELECT * FROM prescriptions")
rows = cur.fetchall()

print("📋 prescriptions table data:\n")
for row in rows:
    print(row)

conn.close()
