from datetime import datetime

birthdate = {
    "day": 0,
    "month": 0,
    "year": 0
}

Date = {
    "day": 0,
    "month": 0,
    "year": 0
}

def get_date():
    Date["day"] = datetime.now().day
    Date["month"] = datetime.now().month
    Date["year"] = datetime.now().year

def get_birthday():

    birthDay = int(input("Please state your birth day: ").strip())
    birthMonth = int(input("Please state your birth month (numerical): ").strip())
    birthYear = int(input("Please state your birth year (yyyy): ").strip())
    set_birthday(birthDay, birthMonth, birthYear)

def set_birthday(birthDay, birthMonth, birthYear):
    birthdate["day"] = birthDay
    birthdate["month"] = birthMonth
    birthdate["year"] = birthYear

def calculate_age():
    age = Date["year"] - birthdate["year"]
    if Date["month"] <= birthdate["month"] and Date["day"] <= birthdate["day"]:
        age -= 1
    print("OMG", get_name() + "! you are", age, "years old. So you were born in", str(birthdate["year"]) + "!")

def get_name():
    name = input("Please enter your name: ").strip()
    return name

def start(): # begins the program calling other relevant functions
    get_date()
    get_birthday()
    calculate_age()

start()

