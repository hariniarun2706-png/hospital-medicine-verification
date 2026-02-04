import sqlite3

# Step 1: Connect to database (illatti auto create aagum)
conn = sqlite3.connect("hospital.db")
cur = conn.cursor()

# Step 2: prescriptions table create pannradhu
cur.execute("""
CREATE TABLE IF NOT EXISTS prescriptions (
    patient_id TEXT PRIMARY KEY,
    medicine_code TEXT NOT NULL,
    high_risk INTEGER CHECK (high_risk IN (0,1)),
    verified INTEGER CHECK (verified IN (0,1))
)
""")

# Step 3: Sample data insert pannradhu
cur.executemany("""
INSERT OR REPLACE INTO prescriptions
(patient_id, medicine_code, high_risk, verified)
VALUES (?, ?, ?, ?)
""", [ ("ram", "MED123", 1, 0),
       ("ram", "MED123", 1, 0)
 ])
# Step 4: Save changes & close DB
conn.commit()
conn.close()

print("✅ hospital.db created with prescriptions table")

