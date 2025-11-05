import modules.database_module as database
import numpy as np
import matplotlib.pyplot as plt

# Admin credentials
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "ADMIN"


def admin_menu():
    # ----------------- Admin Login -----------------
    print("\n===== Admin Login =====")
    username = input("Username: ").strip()
    password = input("Password: ").strip()

    if username != ADMIN_USERNAME or password != ADMIN_PASSWORD:
        print("❌ Invalid admin credentials! Access denied.")
        return  # Exit the menu if login fails

    print(f"\n✅ Welcome, {username}!")

    # ----------------- Admin Dashboard -----------------
    while True:
        print("\n===== Admin Dashboard =====")
        print("1. View all vaccination records")
        print("2. View vaccination statistics")
        print("3. Delete a vaccination record")
        print("4. Add a vaccinator")
        print("5. View all vaccinators")
        print("6. Delete a vaccinator")
        print("7. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            view_all_records()
        elif choice == "2":
            view_statistics()
        elif choice == "3":
            delete_vaccination()
        elif choice == "4":
            add_vaccinator()
        elif choice == "5":
            view_vaccinators()
        elif choice == "6":
            delete_vaccinator()
        elif choice == "7":
            break
        else:
            print("Invalid choice.")


# ----------------- Vaccination Records -----------------
def view_all_records():
    df = database.get_all_records()
    if df.empty:
        print("No records found.")
    else:
        print("\n--- Vaccination Records ---")
        print(df)


def view_statistics():
    df = database.get_all_records()
    if df.empty:
        print("No data for statistics.")
        return

    total = len(df)
    vaccines = df["Vaccine"].unique()
    counts = []

    print("\n--- Vaccination Statistics ---")
    for v in vaccines:
        count = len(df[df["Vaccine"] == v])
        counts.append(count)
        percent = round((count / total) * 100, 2)
        print(f"{v}: {count} people ({percent}%) vaccinated")

    # Bar chart
    plt.bar(vaccines, counts, color='skyblue')
    plt.title("Vaccination Distribution")
    plt.xlabel("Vaccine")
    plt.ylabel("Number of People")
    plt.show()

    # Pie chart
    plt.pie(counts, labels=vaccines, autopct='%1.1f%%', startangle=140)
    plt.title("Vaccination Percentage")
    plt.show()


def delete_vaccination():
    user_id = input("Enter the ID of the record to delete: ").strip()
    success = database.delete_vaccination_record(user_id)
    if success:
        print(f"Record with ID {user_id} deleted successfully.")
    else:
        print(f"No record found with ID {user_id}.")


# ----------------- Vaccinator Management -----------------
def add_vaccinator():
    username = input("Enter new vaccinator username: ").strip()
    password = input("Enter password: ").strip()
    success = database.add_vaccinator(username, password)
    if success:
        print(f"Vaccinator '{username}' added successfully!")
    else:
        print(f"Username '{username}' already exists.")


def view_vaccinators():
    df = database.get_all_vaccinators()
    if df.empty:
        print("No vaccinators registered yet.")
    else:
        print("\n--- Registered Vaccinators ---")
        print(df)


def delete_vaccinator():
    username = input("Enter the username of the vaccinator to delete: ").strip()
    database.delete_vaccinator(username)
    print(f"Vaccinator '{username}' deleted successfully (if existed).")
