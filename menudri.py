# Campus Automation System
# SDG 4: Quality Education | SDG 9: Industry, Innovation & Infrastructure

students = {}
resources = []

# --------------------- MODULE 1: Attendance ---------------------
def manage_attendance():
    while True:
        print("\n--- Attendance Management ---")
        print("1. Mark Attendance")
        print("2. View Attendance")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            student_name = input("Enter student name: ").title()
            status = input("Enter attendance (P/A): ").upper()
            if student_name not in students:
                students[student_name] = []
            students[student_name].append(status)
            print(f"Attendance marked for {student_name}.")
        
        elif choice == "2":
            print("\n--- Attendance Records ---")
            for student, record in students.items():
                print(f"{student}: {record} | Present: {record.count('P')} | Absent: {record.count('A')}")
        
        elif choice == "3":
            break
        else:
            print("Invalid choice! Try again.")

# --------------------- MODULE 2: Digital Resource Management ---------------------
def manage_resources():
    while True:
        print("\n--- Digital Resource Management ---")
        print("1. Add Resource")
        print("2. View Resources")
        print("3. Back to Main Menu")
        choice = input("Enter your choice: ")
        
        if choice == "1":
            resource_name = input("Enter resource name: ")
            resource_type = input("Enter type (Video/PDF/Link): ")
            resources.append({"Name": resource_name, "Type": resource_type})
            print(f"Resource '{resource_name}' added successfully.")
        
        elif choice == "2":
            print("\n--- Available Resources ---")
            for idx, res in enumerate(resources, 1):
                print(f"{idx}. {res['Name']} ({res['Type']})")
        
        elif choice == "3":
            break
        else:
            print("Invalid choice! Try again.")

# --------------------- MODULE 3: Reports ---------------------
def generate_reports():
    print("\n--- Reports ---")
    print("1. Attendance Summary")
    print("2. Resource List")
    choice = input("Enter your choice: ")
    
    if choice == "1":
        print("\n--- Attendance Summary ---")
        if not students:
            print("No attendance records available.")
        else:
            for student, record in students.items():
                print(f"{student}: Present {record.count('P')}, Absent {record.count('A')}")
    
    elif choice == "2":
        print("\n--- Resource List ---")
        if not resources:
            print("No resources available.")
        else:
            for idx, res in enumerate(resources, 1):
                print(f"{idx}. {res['Name']} ({res['Type']})")
    else:
        print("Invalid choice!")

# --------------------- MAIN MENU ---------------------
def main():
    while True:
        print("\n=== Campus Automation System ===")
        print("1. Attendance Management")
        print("2. Digital Resource Management")
        print("3. Generate Reports")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            manage_attendance()
        elif choice == "2":
            manage_resources()
        elif choice == "3":
            generate_reports()
        elif choice == "4":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

# Run the program
if __name__ == "__main__":
    main()
