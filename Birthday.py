from datetime import datetime

# make birthday variable
birthdate = {
    "day": 0,
    "month": 0,
    "year": 0
}

# make date variable
Date = {
    "day": 0,
    "month": 0,
    "year": 0
}

age = int(input("please enter your age: ").strip())

def get_date(): # sets date variable to datetime
    Date["day"] = datetime.now().day
    Date["month"] = datetime.now().month
    Date["year"] = datetime.now().year

def get_birthday(): # gets user birthday

    birthDay = int(input("Please state your birth day: ").strip())
    birthMonth = int(input("Please state your birth month (numerical): ").strip())
    birthYear = int(input("Please state your birth year (yyyy): ").strip())
    set_birthday(birthDay, birthMonth, birthYear)

def set_birthday(birthDay, birthMonth, birthYear): # sets birthday dict to acquired day, month, year from user
    birthdate["day"] = birthDay
    birthdate["month"] = birthMonth
    birthdate["year"] = birthYear

def calculate_age(): # compares birthday against date, then checks if birthday has passed or not, then prints tailored message
    DoB = Date["year"] - age
    # if Date["month"] <= birthdate["month"] and Date["day"] <= birthdate["day"]:
    #     age -= 1
    print("OMG", get_name() + "! you are", str(age), "years old. So you were born in", str(DoB) + "!")

def get_name(): # assigns & returns the user's name from input
    name = input("Please enter your name: ").strip()
    return name

def start(): # begins the program calling other relevant functions
    get_date()
    # get_birthday()
    calculate_age()

start()

