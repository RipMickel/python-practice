import datetime

def get_name():
    while True:
        name = input("What is your name? ").strip()
        if name:
            return name
        print("Name cannot be empty.")

def get_age():
    while True:
        try:
            age = int(input("How old are you? "))
            if 0 <= age <= 120:
                return age
            else:
                print("Enter a realistic age (0–120).")
        except ValueError:
            print("Please enter a valid number.")

def calculate_100_year(age):
    current_year = datetime.datetime.now().year
    return current_year + (100 - age)

def life_stage(age):
    if age < 13:
        return "You're a child 👶"
    elif age < 20:
        return "You're a teenager 😎"
    elif age < 60:
        return "You're an adult 💼"
    else:
        return "You're a senior 🧓"

def fun_fact(age):
    if age % 2 == 0:
        return "Fun fact: Your age is an even number!"
    else:
        return "Fun fact: Your age is an odd number!"

def main():
    print("=" * 40)
    print("   🌟 Welcome to the Smart Profile App 🌟")
    print("=" * 40)

    name = get_name()
    age = get_age()

    print("\n--- Profile Summary ---")
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(life_stage(age))
    print(fun_fact(age))

    year_100 = calculate_100_year(age)

    if age < 100:
        print(f"You will turn 100 in the year {year_100}.")
    elif age == 100:
        print("Amazing! You are 100 this year!")
    else:
        print(f"You turned 100 in the year {year_100}.")

    # Extra feature: countdown
    print("\nCountdown to next birthday 🎂")
    next_bday = age + 1
    print(f"In 1 year, you will be {next_bday} years old!")

    print("\nThanks for using the app. Goodbye!")

if __name__ == "__main__":
    main()