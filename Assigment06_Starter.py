# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add the each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# Roslyn Melookaran,5/20/20,Modified code to add option 1 and 2 script
# Roslyn Melookaran,5/21/20,Modified code to completed assignment 6
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None   # An object that represents a file
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of an processing functions
strExitChoice = ""  # Captures the user confirmation to exit
strExistingItemCheck= "" #Captures 'y' or 'n' if item is in list or not
# Processing  --------------------------------------------------------------- #
class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip().title(), "Priority": priority.strip().title()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(task_append_list, priority_append_list, list_of_rows):
        """ Adds a dictionary row to the list of tasks

        :param task_add_list: (string) task to add:
        :param priority_add_list: (string) priority to add:
        :param list_of_rows: (list) list to append to:
        :return: (list) of dictionary rows
        """
        row={"Task":task_append_list,"Priority":priority_append_list}
        list_of_rows.append(row)
        return list_of_rows, 'Success'

    @staticmethod
    def remove_data_from_list(task_remove_list, list_of_rows):
        """ Removes a dictionary row from task list

                :param task_add_list: (string) task to add:
                :param priority_add_list: (string) priority to add:
                :param list_of_rows: (list) list to append to:
                :return: (list) of dictionary rows
                """
        for i in range(len(list_of_rows)):
            if list_of_rows[i]['Task'] == task_remove_list:
                print("Task: " + list_of_rows[i]["Task"] + ", Priority: " + list_of_rows[i]["Priority"] + ", has been removed")
                del list_of_rows[i]
                break
        return list_of_rows, 'Success'

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        """ Writes data to file

                :param file_name: (string) with name of file:
                :param list_of_rows: (list) data to write to file:
                :return: (list) of dictionary rows
                """
        file = open(file_name, "w")
        for row in list_of_rows:
            file.write(row.get("Task") + ", " + row.get("Priority") + "\n")
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def check_item_existing(task_to_check,list_of_rows):
        """ Checks if item user wants to add is in list

                :param task_to_check: (string) task to add:
                :param list_of_rows: (list) list of rows:
                :return: (string) "Y" or "N"
                """
        for i in range(len(list_of_rows)):
            if list_of_rows[i]['Task'] == task_to_check.title():
                ItemExist="Y"
                break
            else:
                ItemExist="N"

        return ItemExist

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_Tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def input_exit_choice():
        """ Gets the user to confirm they want to exit program

        :return: string
        """
        choice = str(input("Are you sure you are done working with your task list???? (y/n): ")).strip()

        return choice
    @staticmethod
    def print_current_Tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.')

    @staticmethod
    def input_new_task_and_priority():
        """ Gets a task and priority from the user
                :param: Task to be added
                :param: Priority of new task
                :return: task and priority
                """
        task_add= str(input("Please enter the task that you would like to add: ")).strip().title()
        priority_add=str(input("Please enter the prioirty of that task: ")).strip().title()
        return task_add, priority_add

    @staticmethod
    def input_task_to_remove():
        """ Gets a task and priority from the user
                        :param: Task to be removed
                        :return: task
                        """
        task_remove= str(input("Please enter the task that you would like to remove: ")).strip().title()
        return task_remove
        # return task

# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.
Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_Tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_Tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    
    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        # Function that gets the task and priority user wishes to add
        (strTask,strPriority)=IO.input_new_task_and_priority()
        # Function to check if user's task input already exists
        strExistingItemCheck=Processor.check_item_existing(strTask,lstTable)
        # If task already exists, it will not be added
        if strExistingItemCheck=="Y":
            print("Sorry, this item already exists!")
        # If task does not exist-Function that adds the users input to the list
        else:
            Processor.add_data_to_list(strTask,strPriority, lstTable)
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        # Function that gets the task and priority user wishes to remove
        (strTask)=IO.input_task_to_remove()
        # Function to check if user's task input already exists
        strExistingItemCheck = Processor.check_item_existing(strTask, lstTable)
        # If task already exists, it will not be added
        if strExistingItemCheck == "N":
            print("Sorry, this item is not in the list!")
        # If task does not exist-Function that adds the users input to the list
        else:
            # Function that removes the users input from the list
            Processor.remove_data_from_list(strTask, lstTable)

        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            Processor.write_data_to_file(strFileName, lstTable)
            print("Your data has been saved!")
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            Processor.read_data_from_file(strFileName, lstTable)
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  #  Exit Program

        strExitChoice = IO.input_exit_choice()
        if strExitChoice =="y":
            break   # and Exit
        else:
            continue
