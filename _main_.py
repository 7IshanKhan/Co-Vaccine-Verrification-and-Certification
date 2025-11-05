from modules import database_module, client_module, vaccinator_module, admin_module

def main():
    database_module.initialize_database()  # make sure database exists

    while True:
        print("\n===== E-Vaccine Verification System =====")
        print("1. Client")
        print("2. Vaccinator")
        print("3. Admin")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            client_module.client_menu()
        elif choice == "2":
            vaccinator_module.vaccinator_menu()
        elif choice == "3":
            admin_module.admin_menu()
        elif choice == "4":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()
