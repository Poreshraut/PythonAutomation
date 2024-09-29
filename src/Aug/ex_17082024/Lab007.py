 # Ternary operator: A ternary operator is a special kind of operator in programming that works with three operands.
 # It's like a shortcut for making decisions in code.
 # the ternary operator is a quick way to make a decision between two options based on a condition.

weather = "rainy"

print("wear a raincoat" if weather == "rainy" else "wear sunglasses")


age = int(input("Enter your age: "))

print("You can go to Goa" if age > 18 else "You can't go to Gao, stay at Home")

if age >= 18:
    print("can go to Goa")
else:
    print("can't go to Goa, stay at Home")