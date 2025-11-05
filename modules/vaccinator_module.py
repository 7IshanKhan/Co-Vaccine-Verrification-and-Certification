from datetime import datetime
import modules.database_module as database

def vaccinator_menu():
    while True:
        print("\n===== Vaccinator Portal =====")
        print("1. Enter new vaccination record")
        print("2. Back to main menu")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            enter_vaccination_data()
        elif choice == "2":
            break
        else:
            print("Invalid choice, try again.")

def enter_vaccination_data():
    id_ = input("Enter patient ID: ").strip()
    name = input("Enter patient name: ").strip()
    vaccine = input("Enter vaccine name: ").strip()
    dose = input("Enter dose number (1/2): ").strip()
    date = datetime.now().strftime("%Y-%m-%d")

    record = {"ID": id_, "Name": name, "Vaccine": vaccine, "Dose": dose, "Date": date}
    database.add_record(record)
    print("Record added successfully!")
