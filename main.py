from utils import datetime_utils, math_utils, random_utils, uuid_utils, file_utils

def explore_module():
    module_name = input("Enter module name to explore: ")

    try:
        module = __import__(module_name)

        print("Available Attributes in", module_name, "module:")
        print(dir(module))
        print("==========================")

    except:
        print("Module not found")


def main():

    while True:

        print("\n==============================")
        print("Welcome to Multi-Utility Toolkit")
        print("==============================")

        print("Choose an option:")
        print("1. Datetime and Time Operations")
        print("2. Mathematical Operations")
        print("3. Random Data Generation")
        print("4. Generate Unique Identifiers (UUID)")
        print("5. File Operations (Custom Module)")
        print("6. Explore Module Attributes (dir())")
        print("7. Exit")

        choice = input("\nEnter your choice: ")

        match choice:

            case "1":
                datetime_utils.datetime_menu()

            case "2":
                math_utils.math_menu()

            case "3":
                random_utils.random_menu()

            case "4":
                uuid_utils.generate_uuid()

            case "5":
                file_utils.file_menu()

            case "6":
                explore_module()

            case "7":
                print("\n==============================")
                print("Thank you for using the Multi-Utility Toolkit!")
                print("==============================")
                break

            case _:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()