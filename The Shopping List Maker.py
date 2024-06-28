# Objective: The aim of this assignment is to create a program that helps users make a shopping list.
# Task 1: Write a function that lets the user add items to a list.

shopping_list = []

def add_item():
    item = str(input("What item would you like to add to your shopping list? "))
    shopping_list.append(item)
    print(f"{item} has been added to your shopping list.")
    return shopping_list

add_item()


# Task 2: Include a function to remove items from the list.

def remove_item():
    item = str(input("What item would you like to remove from your shopping list? "))
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"{item} has been removed from your shopping list.")
    else:
        print(f"{item} is not in your shopping list.")
    return shopping_list

remove_item()


# Task 3: Add a function that prints out the entire list in a formatted way.

def print_list():
    print("Here is your shopping list:")
    for item in shopping_list:
        print(f"- {item}")
    return shopping_list

print_list()

while True:
    add_or_remove = str(input("Would you like to add, remove, or view shopping list, if not just type in quit to exit? ")).capitalize()
    if add_or_remove == "Add":
        add_item()
        print_list()
    elif add_or_remove == "Remove":
        remove_item()
        print_list()
    elif add_or_remove == "View":
        print_list()
        if len(shopping_list) == 0:
            print("Your shopping list is empty.")
    elif add_or_remove == "Quit":
        print("Thank you for using the Shopping List Maker.")
        break
    else:
        print("Invalid input. Please try again.")
        

    
        
    
     