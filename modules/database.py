import os
import csv

BASE = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data")
CLIENT_FILE = os.path.join(BASE, "clients.csv")
DOCTOR_FILE = os.path.join(BASE, "doctors.csv")

def ensure():
    os.makedirs(BASE, exist_ok=True)
    if not os.path.exists(CLIENT_FILE):
        with open(CLIENT_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["client_id","name","age","gender","vaccine","date","status","doctor_id"])
    if not os.path.exists(DOCTOR_FILE):
        with open(DOCTOR_FILE, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["doctor_id","name","hospital","access_status"])

def read_clients():
    ensure()
    with open(CLIENT_FILE, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def write_clients(rows):
    ensure()
    with open(CLIENT_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["client_id","name","age","gender","vaccine","date","status","doctor_id"])
        writer.writeheader()
        writer.writerows(rows)

def read_doctors():
    ensure()
    with open(DOCTOR_FILE, newline="") as f:
        reader = csv.DictReader(f)
        return list(reader)

def write_doctors(rows):
    ensure()
    with open(DOCTOR_FILE, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["doctor_id","name","hospital","access_status"])
        writer.writeheader()
        writer.writerows(rows)

def find_client(cid):
    for r in read_clients():
        if r["client_id"] == str(cid):
            return r
    return None

def update_client(cid, data):
    rows = read_clients()
    changed = False
    for r in rows:
        if r["client_id"] == str(cid):
            for k,v in data.items():
                if k in r:
                    r[k] = v
            changed = True
    write_clients(rows)
    return changed

def add_client(rec):
    rows = read_clients()
    for r in rows:
        if r["client_id"] == rec["client_id"]:
            return False
    rows.append(rec)
    write_clients(rows)
    return True

def add_doctor(rec):
    rows = read_doctors()
    for r in rows:
        if r["doctor_id"] == rec["doctor_id"]:
            return False
    rows.append(rec)
    write_doctors(rows)
    return True

def set_doctor_status(did, status):
    rows = read_doctors()
    changed = False
    for r in rows:
        if r["doctor_id"] == str(did):
            r["access_status"] = status
            changed = True
    write_doctors(rows)
    return changed
