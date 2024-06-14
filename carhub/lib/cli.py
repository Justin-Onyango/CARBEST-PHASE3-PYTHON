from .helpers import add_car, view_cars, delete_car, update_car, exit_program
    
    

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_car()
        elif choice == "2":
            delete_car()
        elif choice == "3":
            update_car()
        elif choice == "4":
            view_cars()
        else:
            print("Invalid choice, please choose from the prompts provided.")


def menu():
    print("Welcome to CarBest your trusted car dealer! What would you like to do?")
    print("0.Exit")
    print("1. Upload my car")
    print("2. Sell my car")
    print("3. Update my car details")
    print("4. View all my cars")

if __name__ == "__main__":
    main()


