import modules.database_module as database
import modules.certificate_module as certificate

def client_menu():
    while True:
        print("\n===== Client Portal =====")
        print("1. Verify Vaccination Status")
        print("2. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            verify_vaccination()
        elif choice == "2":
            break
        else:
            print("Invalid choice, try again.")

def verify_vaccination():
    user_id = input("Enter your ID: ").strip()
    record = database.verify_vaccination(user_id)

    if record:
        print("\n✅ Vaccination Verified")
        print(f"Name: {record['Name']}")
        print(f"Vaccine: {record['Vaccine']}")
        print(f"Dose: {record['Dose']}")
        print(f"Date: {record['Date']}")

        choice = input("\nDo you want to generate your vaccination certificate? (y/n): ").lower()
        if choice == "y":
            file_name = certificate.generate_certificate(record)
            print(f"Certificate generated successfully: {file_name}")
    else:
        print("\n❌ No vaccination record found for this ID.")
