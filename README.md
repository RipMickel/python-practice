
# 🌟 Smart Profile App

A simple interactive Python CLI application that collects user information and provides fun, personalized insights based on age.

---

## 📌 Features

* 🧑‍💻 User input validation for name and age
* 🎯 Determines life stage (child, teenager, adult, senior)
* 🎲 Fun fact about your age (even or odd)
* 🎉 Calculates the year you will turn (or turned) 100
* 🎂 Birthday countdown to your next age

---

## 🛠️ Requirements

* Python 3.x
* No external libraries required (uses built-in `datetime` module)

---

## ▶️ How to Run

1. Save the script as `main.py`
2. Open your terminal or command prompt
3. Run the program:

```bash
python main.py
```

---

## 💡 How It Works

1. The program asks for your **name** (must not be empty).
2. It asks for your **age**:

   * Must be a number
   * Must be between 0 and 120
3. It then displays:

   * Your profile summary
   * Your life stage
   * A fun fact about your age
   * The year you will turn 100
   * A simple countdown to your next birthday

---

## 🧠 Program Structure

* `get_name()` → Handles name input validation
* `get_age()` → Handles age input validation
* `calculate_100_year(age)` → Computes year when user turns 100
* `life_stage(age)` → Determines life stage category
* `fun_fact(age)` → Returns even/odd age fact
* `main()` → Orchestrates the program flow

---

## 📷 Example Output

```
========================================
   🌟 Welcome to the Smart Profile App 🌟
========================================
What is your name? Alex
How old are you? 25

--- Profile Summary ---
Name: Alex
Age: 25
You're an adult 💼
Fun fact: Your age is an odd number!
You will turn 100 in the year 2099.

Countdown to next birthday 🎂
In 1 year, you will be 26 years old!

Thanks for using the app. Goodbye!
```

---

## 🚀 Future Improvements

* Add support for multiple users
* Store profiles in a file or database
* Add graphical interface (GUI)
* Include more fun facts or statistics

---

## 📄 License

This project is open-source and free to use for learning purposes.

---
