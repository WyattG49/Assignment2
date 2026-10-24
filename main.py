"""
CS 1430 Assignment 2: The Cost of College

All of your Python for this assignment goes in this file.
The student guide explains what to build. Run check.py to test your work.
"""

# ---- CONSTANTS: do not change ----
SEMESTERS_PER_YEAR = 2
MONTHS_PER_YEAR = 9
CLASS_DAYS_PER_SEMESTER = 75
CS1430_CREDITS = 3
CS1430_MEETINGS_PER_SEMESTER = 45


# ---- FUNCTIONS: replace each return 0 ----

def cost_per_semester(annual_cost):
    annual_cost_per_semester = annual_cost / SEMESTERS_PER_YEAR
    return annual_cost_per_semester


def cost_per_month(annual_cost):
    """Give back what one month of the academic year costs."""
    annual_cost_per_month = annual_cost / MONTHS_PER_YEAR
    return annual_cost_per_month


def cost_per_day(annual_cost):
    """Give back what one class day costs."""
    annual_cost_per_day = annual_cost / (CLASS_DAYS_PER_SEMESTER * SEMESTERS_PER_YEAR)
    return annual_cost_per_day


def cost_per_credit(annual_cost, credits):
    """Give back what one credit costs. credits is the number taken this semester."""
    annual_cost_per_credit = (annual_cost / SEMESTERS_PER_YEAR) / credits
    return annual_cost_per_credit


def cost_per_class(annual_cost, credits):
    """Give back what one 50-minute CS 1430 class meeting costs."""
    cost_per_class = (annual_cost / SEMESTERS_PER_YEAR) / credits * CS1430_CREDITS / CS1430_MEETINGS_PER_SEMESTER
    return cost_per_class


def cost_per_minute(annual_cost, credits):
    class_credits = int(input("How many credits is the class? "))
    class_meetings = int(input("How many class meetings are there in the semester? "))
    class_length = int(input("How many minutes is each class meeting? "))
    cost_per_hour = (annual_cost / SEMESTERS_PER_YEAR) / credits * class_credits / class_meetings / class_length
    return cost_per_hour 


# ---- PROGRAM ----

def main():
    total_cost = float(input("Cost for one year of college: "))
    total_credits = int(input("Number of credits per semester: "))

    while True:
        print("Cost per Semester: 1")
        print("Cost per Month: 2")
        print("Cost per Class Day: 3")
        print("Cost per Credit: 4")
        print("Cost per CS 1430 Class Meeting: 5")
        print("Cost per Minute: 6")
        print("Quit: Q")

        choice = input("Choose an option: ")

        if choice == "Q":
            break
        elif choice == "1":
            cost = cost_per_semester(total_cost)
            print(f"Cost per Semester: ${cost:.2f}")
        elif choice == "2":
            cost = cost_per_month(total_cost)
            print(f"Cost per Month: ${cost:.2f}")
        elif choice == "3":
            cost = cost_per_day(total_cost)
            print(f"Cost per Class Day: ${cost:.2f}")
        elif choice == "4":
            cost = cost_per_credit(total_cost, total_credits)
            print(f"Cost per Credit: ${cost:.2f}")
        elif choice == "5":
            cost = cost_per_class(total_cost, total_credits)
            print(f"Cost per CS 1430 Class Meeting: ${cost:.2f}")
        elif choice == "6":
            cost = cost_per_minute(total_cost, total_credits)
            print(f"Cost per Minute: ${cost:.2f}")
        # Add a branch for each menu option here.


# ---- LAUNCH: do not change ----
if __name__ == "__main__":
    main()
