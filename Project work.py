# ===============================
# TRANSPORT MANAGEMENT SYSTEM (STS)
# ===============================

# Pre-existing passengers (given)
passenger_1 = {"name": "Julius", "route": 'AC', "price": 100}
passenger_2 = {"name": "Anita", "route": 'CA', "price": 100}
passenger_3 = {"name": "Eddy", "route": 'AK', "price": 200}
passenger_4 = {"name": "Mills", "route": 'AK', "price": 200}
passenger_5 = {"name": "Papa", "route": 'AC', "price": 100}
passenger_6 = {"name": "Ama", "route": 'KA', "price": 200}

all_passengers = {
    100: passenger_1,
    200: passenger_2,
    300: passenger_3,
    400: passenger_4,
    500: passenger_5,
    600: passenger_6
}

# ===============================
# FUNCTION: Login System
# ===============================
def login():
    correct_pin = "1234"
    attempts = 3

    while attempts > 0:
        pin = input("Enter PIN: ")

        if pin == correct_pin:
            print("Login successful!\n")
            return True
        else:
            attempts -= 1
            print(f"Wrong PIN! Attempts left: {attempts}")

    print("Too many failed attempts. Program exiting.")
    return False


# ===============================
# FUNCTION: Display Menu
# ===============================
def display_menu():
    print("\n***** MENU *****")
    print("A - Add a passenger record")
    print("N - View passenger by name")
    print("V - View all passengers")
    print("P - Passengers per bus")
    print("T - Total ticket sales")
    print("E - Exit")


# ===============================
# FUNCTION: Get price based on route
# ===============================
def get_price(route):
    if route in ['AC', 'CA']:
        return 100
    elif route in ['AK', 'KA']:
        return 200
    else:
        return None


# ===============================
# FUNCTION: Add Passenger
# ===============================
def add_passenger():
    while True:
        name = input("Enter passenger name: ")

        # Give 3 chances for valid route input
        attempts = 3
        while attempts > 0:
            route = input("Enter route (AC, CA, AK, KA): ").upper()

            price = get_price(route)

            if price is not None:
                break
            else:
                attempts -= 1
                print(f"Invalid route! Attempts left: {attempts}")

        if attempts == 0:
            print("Too many invalid inputs. Returning to menu.")
            return

        # Generate next ticket number
        last_ticket = max(all_passengers.keys())
        new_ticket = last_ticket + 100

        # Create new passenger record
        new_passenger = {
            "name": name,
            "route": route,
            "price": price
        }

        # Add to dictionary
        all_passengers[new_ticket] = new_passenger

        # Display new record
        print(f"\n{new_ticket}: {new_passenger}")

        # Ask if user wants to continue
        choice = input("Add another passenger? (yes/no): ").lower()
        if choice != "yes":
            break


# ===============================
# FUNCTION: View Passenger by Name
# ===============================
def view_by_name():
    name = input("Enter passenger name: ").lower()
    found = False

    for ticket, details in all_passengers.items():
        if details["name"].lower() == name:
            print(f"{ticket}: {details}")
            found = True

    if not found:
        print("Passenger not found.")


# ===============================
# FUNCTION: View All Passengers
# ===============================
def view_all():
    for ticket, details in all_passengers.items():
        print(f"{ticket}: {details}")


# ===============================
# FUNCTION: Passengers per Bus
# ===============================
def passengers_per_bus():
    counts = {"AC": 0, "CA": 0, "AK": 0, "KA": 0}

    for details in all_passengers.values():
        route = details["route"]
        counts[route] += 1

    print("\nPassengers per bus")
    for route, count in counts.items():
        print(f"{route} Bus: {count}")


# ===============================
# FUNCTION: Total Ticket Sales
# ===============================
def total_sales():
    total = 0

    for details in all_passengers.values():
        total += details["price"]

    print(f"Total Tickets sold: {total}")


# ===============================
# FUNCTION: Exit Program
# ===============================
def exit_program():
    attempts = 3

    while attempts > 0:
        choice = input("Are you sure you want to exit? (yes/no): ").lower()

        if choice == "yes":
            print("Exiting program...")
            return True
        elif choice == "no":
            return False
        else:
            attempts -= 1
            print(f"Invalid input! Attempts left: {attempts}")

    print("Too many invalid attempts. Returning to menu.")
    return False


# ===============================
# MAIN PROGRAM
# ===============================
if login():
    while True:
        display_menu()

        choice = input("Select an option: ").upper()

        if choice == "A":
            add_passenger()
        elif choice == "N":
            view_by_name()
        elif choice == "V":
            view_all()
        elif choice == "P":
            passengers_per_bus()
        elif choice == "T":
            total_sales()
        elif choice == "E":
            if exit_program():
                break
        else:
            print("Invalid option! Try again.")