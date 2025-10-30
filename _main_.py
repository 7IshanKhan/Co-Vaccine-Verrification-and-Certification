from modules import client_module, doctor_module, admin_module
import sys

def main_menu():
    while True:
        print("""
VACCINE VERIFICATION SYSTEM
1) Client
2) Doctor
3) Admin
4) Exit
""")
        choice = input("Choice: ").strip()
        if choice == "1":
            client_module.client_menu()
        elif choice == "2":
            doctor_module.doctor_menu()
        elif choice == "3":
            ok = input("Admin pass: ").strip()
            if ok == "admin123":
                admin_module.admin_menu()
            else:
                print("Access denied")
        elif choice == "4":
            print("Bye")
            sys.exit(0)
        else:
            print("Invalid")

if __name__ == "__main__":
    main_menu()
