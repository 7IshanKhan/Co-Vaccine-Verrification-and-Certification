import modules.database_module as database
import numpy as np
import matplotlib.pyplot as plt

def admin_menu():
    while True:
        print("\n===== Admin Dashboard =====")
        print("1. View all records")
        print("2. View vaccination statistics")
        print("3. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            view_all_records()
        elif choice == "2":
            view_statistics()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")

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
