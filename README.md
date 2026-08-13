# ☕ Coffee Machine

A beginner Python project that simulates a simple coffee machine. The program allows users to choose a drink, checks available resources, processes coins, handles payments and change, and prepares the selected coffee.

## 📌 Features

- ☕ Choose between espresso, latte, and cappuccino
- 💧 Check available water, milk, and coffee
- 💰 Process coins and calculate the inserted amount
- 💵 Check whether the payment is sufficient
- 🔄 Provide change when excess money is inserted
- 📊 Generate a resource and money report
- ⚙️ Turn the machine off using the `off` command
- ❌ Handle invalid drink selections

## 🛠️ Concepts Practiced

This project was built to practice fundamental Python concepts, including:

- Variables and data types
- Dictionaries and nested dictionaries
- Functions
- `for` and `while` loops
- Conditional statements
- User input
- Return values
- Exception handling with `try` / `except`
- Basic arithmetic and program flow

## ☕ Available Drinks

| Drink | Water | Milk | Coffee | Cost |
|---|---:|---:|---:|---:|
| Espresso | 50ml | — | 18g | $1.50 |
| Latte | 200ml | 150ml | 24g | $2.50 |
| Cappuccino | 250ml | 100ml | 24g | $3.00 |

## 💵 Coin Values

The machine accepts:

- Quarter = $0.25
- Dime = $0.10
- Nickel = $0.05
- Penny = $0.01

If the amount inserted is greater than the drink's cost, the machine calculates and returns the change.

## 📊 Machine Resources

The machine starts with:

- Water: 300ml
- Milk: 200ml
- Coffee: 100g
- Money: $0.00

Resources are automatically deducted when a drink is successfully purchased.

## ▶️ How to Run

Make sure Python is installed on your computer.

Run the program from the terminal:

```bash
python main.py
```

Then follow the prompts to select a drink and enter the required coins.

### Special Commands

```text
report
```

Displays the current resources and money collected.

```text
off
```

Turns off the coffee machine.

## 🎯 Project Purpose

This project was created as a **beginner Python practice project** to apply fundamental programming concepts in a small, functional application.

The project is inspired by the Coffee Machine project from **100 Days of Code: The Complete Python Pro Bootcamp** by Angela Yu.

## 📌 Project Status

Completed as a beginner Python practice project.
