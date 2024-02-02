

# Project 1: How old was I?
# This small program will ask you to input your birth year and any year after your birth year.
# it will tell you how old you were on any given year.d
# I've included input validation and error handling.



def how_old(birth_year, selected_year):
    try:
        if selected_year >= birth_year:
            my_age = selected_year - birth_year
            return f"In {selected_year}, you were {my_age} years old!"
        else:
            return "Invalid Input: Selected year is before your birth year."
    except ValueError:
        return "Invalid Input: Please enter a valid Year YYYY."

def get_birth_year():
    while True:
        birth_year = input("Enter your birth year (4 digits): ")
        if len(birth_year) == 4 and birth_year.isdigit():
            return int(birth_year)
        else:
            print("Invalid Input. Please enter a 4-digit year.")


birth_year = get_birth_year()
selected_year = int(input("Enter a year: "))

age_result = how_old(birth_year, selected_year)
print(age_result)

