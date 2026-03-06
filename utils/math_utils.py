import math

def math_menu():

    while True:

        print("\nMathematical Operations:")
        print("1. Calculate Factorial")
        print("2. Solve Compound Interest")
        print("3. Trigonometric Calculations")
        print("4. Area of Geometric Shapes")
        print("5. Back to Main Menu")

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                n = int(input("\nEnter a number: "))
                print("Factorial:", math.factorial(n))
                print("==========================")

            case "2":
                p = float(input("\nEnter principal amount: "))
                r = float(input("Enter rate of interest (in %): "))
                t = float(input("Enter time (in years): "))

                ci = p * pow((1 + r/100), t)
                print("Compound Interest:", format(ci,".2f"))
                print("==========================")

            case "3":
                angle = float(input("Enter angle in degrees: "))
                rad = math.radians(angle)

                print("sin:",math.sin(rad))
                print("cos:",math.cos(rad))
                print("tan:",math.tan(rad))

            case "4":
                r = float(input("Enter radius: "))
                area = math.pi * r * r
                print("Area:",area)

            case "5":
                break