import random
import string

def random_menu():

    while True:

        print("\nRandom Data Generation:")
        print("1. Generate Random Number")
        print("2. Generate Random List")
        print("3. Create Random Password")
        print("4. Generate Random OTP")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                print("Random Number:",random.randint(1,100))

            case "2":
                lst=[random.randint(1,50) for i in range(5)]
                print("Random List:",lst)

            case "3":
                length=int(input("Enter password length: "))
                chars=string.ascii_letters+string.digits+"!@#$%"
                password="".join(random.choice(chars) for i in range(length))

                print("Generated Password:",password)
                print("==========================")

            case "4":
                otp=random.randint(100000,999999)
                print("Generated OTP:",otp)

            case "5":
                break