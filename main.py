import sqlite3

# Connect to hospital database
conn = sqlite3.connect("hospital.db")
cur = conn.cursor()

def verify_medicine():
    patient_id = input("Scan Patient Barcode: ").strip().upper()
    medicine_barcode = input("Scan Medicine Barcode: ").strip().upper()

    cur.execute("""
    SELECT medicine_code, high_risk, verified
    FROM prescriptions
    WHERE patient_id = ?
    """, (patient_id,))

    record = cur.fetchone()

    if not record:
        print("❌ Prescription not found for this patient")
        return

    prescribed_code, high_risk, verified = record

    if high_risk == 1 or verified == 0:
        if medicine_barcode == prescribed_code:
            print("✅ POSITIVE VERIFICATION")
            print("Correct medicine – Safe to administer")

            cur.execute("""
            UPDATE prescriptions
            SET verified = 1
            WHERE patient_id = ?
            """, (patient_id,))
            conn.commit()
        else:
            print("🚨 NEGATIVE VERIFICATION")
            print("WRONG MEDICINE – DO NOT ADMINISTER")
    else:
        print("ℹ️ Medicine already verified earlier")
        print("Proceed without re-scanning")

verify_medicine()
conn.close()