from time import sleep
import os
from SingleLinkedList_Class import SingleLinkedList
from Node_Class import Node

class PurchaseItem(Node): # class inherited from class 'Node' which will contain additional information
    def __init__(self, value=None, amount=1, price=0.0):
        super().__init__(value)
        self.amount = amount
        self.price = price   

################################# Functions used in the program #################################
def totalSum(list=SingleLinkedList()):
    sumAmount = 0
    sumPrice = 0
    for item in list:
        sumAmount += item.amount
        sumPrice += item.amount * item.price
    return {'sumAmount':sumAmount, 'sumPrice':sumPrice}

def clearScreen(): # Clear the screen
    os.system('cls' if os.name == 'nt' else 'clear')

def commandIsValid(userCommand, commandsDefault=[]): # function to check if the command is valid
    if userCommand in commandsDefault:
        return True
    
def personalizerItem(item=PurchaseItem(None)):
    return f"|{str(item.value).ljust(19, ' ')}|{str(item.amount).ljust(6, ' ')}| ${item.price:>7.2f}|"

def showShoppingList():
    """ Print the List of Items in a table format """
    print(" Shooping List ".center(38, "="))
    print('_'*38)
    # Print the header of the table
    print(f"|{'Description'.ljust(19, ' ')}|{'Amount'.ljust(6, ' ')}|{'Price'.ljust(9, ' ')}|")
    print('_'*38)
    # Print all items in the list
    for item in listOfItems:
        print(personalizerItem(item))
    print('_'*38)
    # Print a line with the total amount of items and the total price
    print(f"|{'Total'.ljust(19, ' ')}|{str(totalSum(listOfItems)['sumAmount']).ljust(6, ' ')}| ${totalSum(listOfItems)['sumPrice']:>7.2f}|")
    print('_'*38)
    print("=" * 38)


################################# Main program #################################

listOfItems = SingleLinkedList()

while True:
    clearScreen()
    showShoppingList()

    """ Ask the user what he wants to do """
    print("What do you want to do?")
    print("1 - Add item")
    print("2 - Remove item")
    print("3 - Edit item")
    print("4 - Clear list")
    print("5 - Exit")

    while True:
        userCommand = input("Command: ")
        if commandIsValid(userCommand, ["1", "2", "3", "4", "5"]):
            break
        else:
            print("Invalid command. Insert '1', '2', '3', '4' or '5'")

    if userCommand =='1': # Add item
        clearScreen()
        print("Ok! Let's add an item!".center(38, "="))
        itemName = input("Name of Item: ")
        itemAmount = int(input("Amount: "))
        itemPrice = float(input("Price: "))
        if(listOfItems.insertNode(PurchaseItem(itemName, itemAmount, itemPrice), -1)):
            print("Item added successfully!")
            sleep(2)

    elif userCommand =='2': # Remove item
        clearScreen()
        print("Ok! Let's remove an item!".center(38, "="))
        showShoppingList()
        itemName = input("\nName of Item: ")

        positionOfItem = listOfItems.searchNode(itemName)[1]
        if positionOfItem == -1:
            print("Item not found!")
            sleep(2)
        else:
            print("Item removed successfully!")
            listOfItems.deleteNode(positionOfItem)
            sleep(2)

    elif userCommand =='3': # Edit item
        clearScreen()
        print("Ok! Let's edit an item!".center(38, "="))
        showShoppingList()
        itemName = input("\nName of Item: ")
        nodeOfItem = listOfItems.searchNode(itemName)[0]
        if nodeOfItem is not None:
            print(personalizerItem(nodeOfItem))
            print("What do you want to edit?")
            print("1 - Name")
            print("2 - Amount")
            print("3 - Price")
            while True:
                userCommand = input("Command: ")
                if commandIsValid(userCommand, ["1", "2", "3"]):
                    break
                else:
                    print("Invalid command. Insert '1', '2' or '3'")
            if userCommand == '1':
                newName = input("New name: ")
                nodeOfItem.value = newName
            elif userCommand == '2':
                newAmount = int(input("New amount: "))
                nodeOfItem.amount = newAmount
            elif userCommand == '3':
                newPrice = float(input("New price: "))
                nodeOfItem.price = newPrice
            print("Item edited successfully!")
            sleep(2)
        else:
            print("Item not found!")
            sleep(2)
            continue

    elif userCommand =='4': # Clear list
        clearScreen()
        showShoppingList()
        print("Are you sure you want to clear the list?")
        print("1 - Yes")
        print("2 - No")
        while True:
            userCommand = input("Command: ")
            if commandIsValid(userCommand, ["1", "2"]):
                break
            else:
                print("Invalid command. Insert '1' or '2'")
        if userCommand == '1':
            listOfItems.deleteEntireSLL()
            print("List cleared successfully!")
            sleep(2)
        else:
            continue

    else:
        print("Goodbye!")
        break
