menu = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}




def report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")


def processing_coins():
    quarters=int (input("How many quarters?:"))
    dimes=int (input("How many dimes?:"))
    nickles=int (input("How many nickles?:"))
    pennies=int (input("How many pennies?:"))
    input_amt=quarters*0.25+dimes*0.1+nickles*0.05+pennies*0.01
    return input_amt

def is_resources_enough(drink_ingredients):
    for item in drink_ingredients:
        if drink_ingredients[item]>resources[item]:
            print(f"Sorry, there is not enough {item}.")
            return False
    return True

    
def make_coffee(drink_ingredients):
    for item in drink_ingredients:
        resources[item]-=drink_ingredients[item]

money=0.00
while True:
    
    coffee=input("What would you like? (espresso/latte/cappuccino):").lower()
    try:
        if coffee=='off':
            print("Turning off")
            break
        elif coffee=='report':
            report()
        else:
            drink=menu[coffee]
            if is_resources_enough(drink['ingredients']):
        
                input_amt=processing_coins()
            
                if input_amt>=drink['cost']:
                
                    make_coffee(drink["ingredients"])
                    money+=drink['cost']
                    print(f"Here is your {coffee}☕.Enjoy.")
                    if input_amt>drink['cost']:
                        change=round(input_amt-drink['cost'], 2)
                        print(f"Here's Your Change: {change:.2f}")




                else:
                    print("Sorry, that's not enough money.  Money refunded")
    except KeyError:
        print("Invalid selection. Please choose espresso, latte, or cappuccino.")