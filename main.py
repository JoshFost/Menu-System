print ("Inventory Management Menu")
print ("1. View Inventory ")
print ("2. Add an item ")
print ("3. Edit an item")
print ("4. Exit")
menu_choice = int(input("Please select a number for the menu item you want.(1-4)\n"))
print(menu_choice)
#add inventory

def add_item(addeditem):
    item = input("Enter the name of the item you would like to add. ")