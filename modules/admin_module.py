from . import database
from datetime import datetime
import os

def view_all_records():
    rows = database.read_clients()
    if not rows:
        print("No clients")
        return
    print("id | name | age | gender | vaccine | date | status | doctor")
    for r in rows:
        print(r["client_id"], "|", r["name"], "|", r["age"], "|", r["gender"], "|", (r["vaccine"] or "-"), "|", (r["date"] or "-"), "|", r["status"], "|", (r["doctor_id"] or "-"))

def view_doctors():
    rows = database.read_doctors()
    if not rows:
        print("No doctors")
        return
    print("id | name | hospital | status")
    for r in rows:
        print(r["doctor_id"], "|", r["name"], "|", r["hospital"], "|", r["access_status"])

def add_doctor():
    did = input("Doctor ID: ").strip()
    name = input("Name: ").strip()
    hosp = input("Hospital: ").strip()
    rec = {"doctor_id": did, "name": name, "hospital": hosp, "access_status": "Approved"}
    ok = database.add_doctor(rec)
    if ok:
        print("Added")
    else:
        print("Exists")

def revoke_doctor():
    did = input("Doctor ID to revoke: ").strip()
    ok = database.set_doctor_status(did, "Revoked")
    if ok:
        print("Revoked")
    else:
        print("Not found")

def approve_doctor():
    did = input("Doctor ID to approve: ").strip()
    ok = database.set_doctor_status(did, "Approved")
    if ok:
        print("Approved")
    else:
        print("Not found")

def generate_report():
    rows = database.read_clients()
    total = len(rows)
    vaccinated = sum(1 for r in rows if r["status"].lower() == "verified")
    pending = total - vaccinated
    docs = {}
    for r in rows:
        did = r["doctor_id"] or "-"
        docs.setdefault(did, 0)
        if r["status"].lower() == "verified":
            docs[did] += 1
    print("Total:", total)
    print("Vaccinated:", vaccinated)
    print("Pending:", pending)
    print("Verifications by doctor:")
    for d,k in docs.items():
        print(d, k)

def backup_database():
    base = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "backup")
    os.makedirs(base, exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    src_c = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "clients.csv")
    src_d = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "doctors.csv")
    dst_c = os.path.join(base, f"clients_{ts}.csv")
    dst_d = os.path.join(base, f"doctors_{ts}.csv")
    if os.path.exists(src_c):
        with open(src_c, "r") as s, open(dst_c, "w") as d:
            d.write(s.read())
    if os.path.exists(src_d):
        with open(src_d, "r") as s, open(dst_d, "w") as d:
            d.write(s.read())
    print("Backup done:", base)

def admin_menu():
    while True:
        print("""
ADMIN MENU
1) View all records
2) View doctors
3) Approve doctor
4) Revoke doctor
5) Add doctor
6) Generate report
7) Backup
8) Back
""")
        c = input("Choice: ").strip()
        if c == "1":
            view_all_records()
        elif c == "2":
            view_doctors()
        elif c == "3":
            approve_doctor()
        elif c == "4":
            revoke_doctor()
        elif c == "5":
            add_doctor()
        elif c == "6":
            generate_report()
        elif c == "7":
            backup_database()
        elif c == "8":
            break
        else:
            print("Invalid")
