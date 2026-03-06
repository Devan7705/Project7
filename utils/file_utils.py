import os

def file_menu():
    while True:
        print("\nFile Operations:")
        print("1. Create a new file")
        print("2. Write to a file")
        print("3. Read from a file")
        print("4. Append to a file")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        match choice:
            case "1":
                name = input("Enter file name: ")
                open(name, "w").close()
                print("File created successfully!")

            case "2":
                name = input("Enter file name: ")
                data = input("Enter data to write: ")
                with open(name, "w") as f:
                    f.write(data)
                print("Data written successfully!")

            case "3":
                name = input("Enter file name: ")
                if os.path.exists(name):
                    with open(name, "r") as f:
                        print("File Content:")
                        print(f.read())
                else:
                    print("File does not exist")

            case "4":
                name = input("Enter file name: ")
                data = input("Enter data to append: ")
                with open(name, "a") as f:
                    f.write(data)
                print("Data appended successfully!")

            case "5":
                break