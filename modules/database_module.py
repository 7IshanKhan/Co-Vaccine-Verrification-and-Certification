import pandas as pd
import os

# File paths
db_file = os.path.join(os.path.dirname(__file__), '..', 'vaccination_data.csv')
vaccinator_file = os.path.join(os.path.dirname(__file__), '..', 'vaccinators.csv')

# ----------------- Initialization -----------------
def initialize_database():
    # Vaccination data
    if not os.path.exists(db_file):
        df = pd.DataFrame(columns=["ID", "Name", "Vaccine", "Dose", "Date"])
        df.to_csv(db_file, index=False)
    # Vaccinator accounts
    if not os.path.exists(vaccinator_file):
        df = pd.DataFrame(columns=["Username", "Password"])
        df.to_csv(vaccinator_file, index=False)

# ----------------- Vaccination Data -----------------
def add_record(data):
    df = pd.read_csv(db_file)
    # Ensure ID is string
    data["ID"] = str(data["ID"])
    df = pd.concat([df, pd.DataFrame([data])], ignore_index=True)
    df.to_csv(db_file, index=False)

def verify_vaccination(user_id):
    df = pd.read_csv(db_file)
    df["ID"] = df["ID"].astype(str)
    record = df[df["ID"] == str(user_id)]
    if not record.empty:
        return record.iloc[0].to_dict()
    return None

def get_all_records():
    df = pd.read_csv(db_file)
    # Ensure ID column is string
    df["ID"] = df["ID"].astype(str)
    return df

def delete_vaccination_record(user_id):
    if not os.path.exists(db_file):
        return False
    df = pd.read_csv(db_file)
    df["ID"] = df["ID"].astype(str)
    if str(user_id) not in df["ID"].values:
        return False
    df = df[df["ID"] != str(user_id)]
    df.to_csv(db_file, index=False)
    return True

# ----------------- Vaccinator Accounts -----------------
def add_vaccinator(username, password):
    df = pd.read_csv(vaccinator_file)
    if username in df['Username'].values:
        return False
    df = pd.concat([df, pd.DataFrame([{"Username": username, "Password": password}])], ignore_index=True)
    df.to_csv(vaccinator_file, index=False)
    return True

def verify_vaccinator(username, password):
    df = pd.read_csv(vaccinator_file)
    record = df[(df['Username'] == username) & (df['Password'] == password)]
    return not record.empty

def get_all_vaccinators():
    return pd.read_csv(vaccinator_file)

def delete_vaccinator(username):
    df = pd.read_csv(vaccinator_file)
    df = df[df['Username'] != username]
    df.to_csv(vaccinator_file, index=False)
