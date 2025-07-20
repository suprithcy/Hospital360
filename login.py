import os

def main_menu():
    print("\n🟩 Welcome to ONYX Hospital Application 🏥")
    print("----------------------------------------")
    print("1. Receptionist Login")
    print("2. Doctor Login")

    try:
        choice = int(input("\nEnter your choice (1 or 2): "))
        if choice == 1:
            os.system('python Hospital_Reception_System.py')
        elif choice == 2:
            os.system('python Doctor_view.py')
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")
    except ValueError:
        print("❌ Invalid input. Please enter a number.")

if __name__ == "__main__":
    main_menu()
