import datetime
import time

def datetime_menu():
    while True:
        print("\nDatetime and Time Operations:")
        print("1. Display current date and time")
        print("2. Calculate difference between two dates/times")
        print("3. Format date into custom format")
        print("4. Stopwatch")
        print("5. Countdown Timer")
        print("6. Back to Main Menu")

        choice = input("Enter your choice: ")

        match choice:

            case "1":
                now = datetime.datetime.now()
                print("\nCurrent Date and Time:", now.strftime("%Y-%m-%d %H:%M:%S"))
                print("==========================")

            case "2":
                d1 = input("\nEnter the first date (YYYY-MM-DD): ")
                d2 = input("Enter the second date (YYYY-MM-DD): ")

                date1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
                date2 = datetime.datetime.strptime(d2, "%Y-%m-%d")

                diff = (date2 - date1).days
                print("Difference:", diff, "days")
                print("==========================")

            case "3":
                d = input("Enter date (YYYY-MM-DD): ")
                date_obj = datetime.datetime.strptime(d, "%Y-%m-%d")
                print("Formatted Date:", date_obj.strftime("%d-%m-%Y"))
                print("==========================")

            case "4":
                input("Press Enter to start stopwatch")
                start = time.time()
                input("Press Enter to stop stopwatch")
                end = time.time()
                print("Elapsed Time:", round(end - start,2),"seconds")

            case "5":
                sec = int(input("Enter countdown seconds: "))
                while sec>0:
                    print(sec)
                    time.sleep(1)
                    sec-=1
                print("Time's up!")

            case "6":
                break