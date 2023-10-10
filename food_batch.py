class FoodPackage:
    def __init__(self, name, taste):
        self.name = name
        self.taste = taste

def create_food_packages():
    # Create a list of food packages with names and tastes
    packages = [
        FoodPackage("Package A", "Savory"),
        FoodPackage("Package B", "Sweet"),
        FoodPackage("Package C", "Spicy"),
        FoodPackage("Package D", "Sour"),
        # Add more packages as needed
    ]
    return packages

def check_nausea(packages_consumed, new_package):
    # Check if consuming the new package with any of the existing packages
    # will result in nausea (i.e., combining different tastes)
    for package in packages_consumed:
        if package.taste != new_package.taste:
            return True
    return False

def main():
    food_packages = create_food_packages()
    consumed_packages = []

    print("Welcome to the Food Intake Manager!")

    while True:
        print("\nAvailable Food Packages:")
        for i, package in enumerate(food_packages, start=1):
            print(f"{i}. {package.name} ({package.taste})")

        choice = input("Enter the number of the package you want to consume (or 'q' to quit): ")

        if choice.lower() == 'q':
            break

        try:
            package_index = int(choice) - 1
            if 0 <= package_index < len(food_packages):
                selected_package = food_packages[package_index]
                if not check_nausea(consumed_packages, selected_package):
                    print(f"You are enjoying {selected_package.name} ({selected_package.taste})")
                    consumed_packages.append(selected_package)
                else:
                    print("Caution: Mixing different tastes may cause nausea. Please choose another package.")
            else:
                print("Invalid package number. Please choose a valid package.")
        except ValueError:
            print("Invalid input. Please enter a valid number or 'q' to quit.")

    print("Thank you for using the Food Intake Manager!")

if __name__ == "__main__":
    main()
