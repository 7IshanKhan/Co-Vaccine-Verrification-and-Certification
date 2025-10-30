from . import database
import uuid
from datetime import datetime

def register_client():
    name = input("Full name: ").strip()
    age = input("Age: ").strip()
    gender = input("Gender (M/F/O): ").strip()
    cid = str(uuid.uuid4())[:8]
    rec = {
        "client_id": cid,
        "name": name,
        "age": age,
        "gender": gender,
        "vaccine": "",
        "date": "",
        "status": "Pending",
        "doctor_id": ""
    }
    ok = database.add_client(rec)
    if ok:
        print("Registered. Your ID:", cid)
    else:
        print("Registration failed")

def login_client():
    cid = input("Enter ID: ").strip()
    r = database.find_client(cid)
    if not r:
        print("Not found")
        return None
    return r

def view_status():
    r = login_client()
    if not r:
        return
    print("ID:", r["client_id"])
    print("Name:", r["name"])
    print("Vaccine:", r["vaccine"] or "N/A")
    print("Date:", r["date"] or "N/A")
    print("Status:", r["status"])
    if r["status"].lower() == "verified":
        print("Verified by doctor ID:", r["doctor_id"])

def view_certificate():
    r = login_client()
    if not r:
        return
    if r["status"].lower() != "verified":
        print("Certificate not available. Status:", r["status"])
        return
    print("------ VACCINATION CERTIFICATE ------")
    print("Name:", r["name"])
    print("ID:", r["client_id"])
    print("Vaccine:", r["vaccine"])
    print("Date:", r["date"])
    print("Doctor ID:", r["doctor_id"])
    print("-------------------------------------")

def update_profile():
    r = login_client()
    if not r:
        return
    new_name = input(f"Name [{r['name']}]: ").strip() or r['name']
    new_age = input(f"Age [{r['age']}]: ").strip() or r['age']
    new_gender = input(f"Gender [{r['gender']}]: ").strip() or r['gender']
    database.update_client(r["client_id"], {"name": new_name, "age": new_age, "gender": new_gender})
    print("Updated")

def client_menu():
    while True:
        print("""
CLIENT MENU
1) Register
2) View Status
3) View Certificate
4) Update Profile
5) Back
""")
        c = input("Choice: ").strip()
        if c == "1":
            register_client()
        elif c == "2":
            view_status()
        elif c == "3":
            view_certificate()
        elif c == "4":
            update_profile()
        elif c == "5":
            break
        else:
            print("Invalid")
