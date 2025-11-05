import modules.database_module as database
from datetime import datetime

def vaccinator_menu():
    print("\n===== Vaccinator Login =====")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if not database.verify_vaccinator(username, password):
        print("Invalid username or password!")
        return

    print(f"\nWelcome, {username}!")
    while True:
        print("\n1. Enter new vaccination record")
        print("2. Logout")
        choice = input("Enter choice: ").strip()
        if choice == "1":
            enter_vaccination_data()
        elif choice == "2":
            break
        else:
            print("Invalid choice.")

def enter_vaccination_data():
    id_ = input("Enter patient ID: ").strip()
    name = input("Enter patient name: ").strip()
    vaccine = input("Enter vaccine name: ").strip()
    dose = input("Enter dose number (1/2): ").strip()
    date = datetime.now().strftime("%Y-%m-%d")

    record = {"ID": id_, "Name": name, "Vaccine": vaccine, "Dose": dose, "Date": date}
    database.add_record(record)
    print("Record added successfully.")
