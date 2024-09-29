print("My name is Poresh")

def make_pizza(*toppings, base):
    print(toppings, base)


make_pizza("tomato", "garlic", "Chilly", "cheese", base="Crust")

def make_pizz2(*toppings2):
    for topping in toppings2:
        print(topping)

make_pizz2("Tomato", "Onion", "Chilly", "Paper")