import pandas as pd
import os

# Absolute path ensures all modules read/write the same CSV
db_file = os.path.join(os.path.dirname(__file__), '..', 'vaccination_data.csv')

def initialize_database():
    """Create CSV if it doesn't exist"""
    if not os.path.exists(db_file):
        df = pd.DataFrame(columns=["ID", "Name", "Vaccine", "Dose", "Date"])
        df.to_csv(db_file, index=False)

def add_record(data):
    """Add new vaccination record"""
    if not os.path.exists(db_file):
        initialize_database()
    df = pd.read_csv(db_file)
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_csv(db_file, index=False)

def verify_vaccination(user_id):
    """Return record by ID"""
    if not os.path.exists(db_file):
        return None
    df = pd.read_csv(db_file)
    if df.empty:
        return None
    df["ID"] = df["ID"].astype(str)  # convert all IDs to string
    record = df[df["ID"] == str(user_id)]
    if not record.empty:
        return record.iloc[0].to_dict()
    return None

def get_all_records():
    """Return all records as DataFrame"""
    if not os.path.exists(db_file):
        initialize_database()
    return pd.read_csv(db_file)
