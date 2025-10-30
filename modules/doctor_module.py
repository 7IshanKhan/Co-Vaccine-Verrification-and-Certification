from . import database
from datetime import datetime

def doctor_login():
    did = input("Doctor ID: ").strip()
    docs = database.read_doctors()
    for d in docs:
        if d["doctor_id"] == did and d["access_status"].lower() == "approved":
            return d
    print("Invalid or not approved")
    return None

def record_vaccination():
    d = doctor_login()
    if not d:
        return
    cid = input("Client ID: ").strip()
    client = database.find_client(cid)
    if not client:
        print("Client not found")
        return
    if client["status"].lower() == "verified":
        print("Already verified")
        return
    vaccine = input("Vaccine name: ").strip()
    date = input("Date (YYYY-MM-DD) [leave empty for today]: ").strip()
    if not date:
        date = datetime.today().strftime("%Y-%m-%d")
    database.update_client(cid, {"vaccine": vaccine, "date": date, "status": "Verified", "doctor_id": d["doctor_id"]})
    print("Recorded")

def list_pending():
    docs = database.read_doctors()
    did = input("Doctor ID: ").strip()
    ok = False
    for d in docs:
        if d["doctor_id"] == did and d["access_status"].lower() == "approved":
            ok = True
    if not ok:
        print("Not approved")
        return
    clients = database.read_clients()
    for c in clients:
        if c["status"].lower() != "verified":
            print(c["client_id"], c["name"], c["status"])
    print("End")

def register_doctor():
    did = input("New doctor ID: ").strip()
    name = input("Name: ").strip()
    hosp = input("Hospital: ").strip()
    rec = {"doctor_id": did, "name": name, "hospital": hosp, "access_status": "Pending"}
    ok = database.add_doctor(rec)
    if ok:
        print("Doctor registered, pending approval")
    else:
        print("Doctor exists")

def doctor_menu():
    while True:
        print("""
DOCTOR MENU
1) Login & Record Vaccination
2) List Pending Clients
3) Register as Doctor
4) Back
""")
        c = input("Choice: ").strip()
        if c == "1":
            record_vaccination()
        elif c == "2":
            list_pending()
        elif c == "3":
            register_doctor()
        elif c == "4":
            break
        else:
            print("Invalid")
