from enum import Enum
import csv
import os
from colored_print import prGreen, prRed, prCyan, prYellow, prLightPurple, prPurple, prLightGray, prBlack

csv_filename = "car_data.csv"
csv_path = os.path.join(os.path.dirname(__file__), csv_filename)

class Action(Enum):
    ADD = 1
    SEARCH = 2
    CLEAR = 3
    PRINT_ALL = 4
    EXIT = 5
    UPDATE = 6
    STOCK = 7 

new_list = []

def display():
    prCyan("1-ADD\n2-SEARCH\n3-CLEAR\n4-PRINT_ALL\n5-EXIT\n6-UPDATE_MODEL\n7-CARS_IN_STOCK")
    return Action(int(input("What do you want to do today? Enter the number: ")))

def carsInStock():
    prYellow(f"Number of cars in stock: {len(new_list)-1}")

def addData():
    while True:
        user_selection = display()
        if user_selection == Action.ADD:
            company = input("Write a company: ")
            color = input("Write color: ")
            model = input("Write a model: ")
            new_item = [company, color, model]
            new_list.append(new_item)
            prGreen("New item added")
            saveToCSV()
        elif user_selection == Action.SEARCH:
            searchData()
        elif user_selection == Action.PRINT_ALL:
            printall()
        elif user_selection == Action.EXIT:
            saveToCSV()
            break
        if user_selection== Action.UPDATE:
            updateModel()
        if user_selection== Action.STOCK:
            carsInStock()
        elif user_selection == Action.CLEAR:
            clearChoice = input("Press 8 to DELETE the LAST ONE OR\nPress 9 to choose a name: ")
            if clearChoice == "8":
                if new_list:
                    removed_item = new_list.pop()
                    saveToCSV()
                    prGreen(f'Car: {removed_item[0]}, Successfully removed from the list!')
                    printall()
                else:
                    prRed("The list is empty, nothing to remove.")
            elif clearChoice == "9":
                prPurple("Available names:")
                with open(csv_path, 'r') as csvfile:
                    csv_reader = csv.reader(csvfile)
                    for row in csv_reader:
                        if row:
                            prPurple(row[0])
                selected_name = input("Choose a name to delete: ")
                found = False
                for item in new_list:
                    if len(item) > 0 and item[0] == selected_name:
                        new_list.remove(item)
                        saveToCSV()
                        prRed(f'Car: {selected_name}, Successfully removed from the list!')
                        found = True
                        printall()
                if not found:
                    prRed("Car not found in the list.")
            else:
                prRed("Invalid input. No action taken.")



def printall():
    prYellow("Contents of the list:")
    for item in new_list:
        prPurple(item)

def searchData():
    term = input("Enter a name to search: ").strip()
    found = False

    with open(csv_path, 'r') as csvfile:
        csv_reader = csv.reader(csvfile)
        for row in csv_reader:
            if row and row[0].strip() == term:
                prYellow(f'item :{row} in the list ')
                found = True
                break

    if not found:
        prRed("No matching items found.")



def saveToCSV():
    with open(csv_path, "w", newline="") as csvfile:
        csv_writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csv_writer.writerows(new_list)
    prGreen("Data saved to CSV file.")

def loadFromCSV():
    try:
        with open(csv_path, "r") as csvfile:
            csv_reader = csv.reader(csvfile)
            for line in csv_reader:
                new_list.append(line)
                prPurple(line)
        prGreen("Data loaded from CSV file.")
    except FileNotFoundError:
        prRed("CSV file not found.")

def clearTerminal():
    os.system("clear")
    
def updateModel():
    term = input("Enter a company to update its model year: ").strip()
    new_model_year = input("Enter the new model year: ").strip()

    updated = False
    for item in new_list:
        if len(item) > 0 and item[0] == term:
            item[2] = new_model_year
            saveToCSV()
            prGreen(f'Model year for {term} updated to {new_model_year}')
            updated = True
            break

    if not updated:
        prRed("Car not found in the list.")


if __name__ == "__main__":
    clearTerminal()
    loadFromCSV()
    input("Press Enter to continue...")
    clearTerminal()
    addData()
    input("Press Enter to continue...")
    clearTerminal()
    saveToCSV()
    input("Press Enter to continue...")


## קובץ read me  
# להוסיך היערות 

