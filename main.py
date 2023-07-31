
def print_menu(choices):
    for index, choice in enumerate(choices, start=1):
        print(f"{index}. {choice}")
    choices_list = ["Option 1"], ["Option 2"], ["Option 3"]
    print("Please select one or more options from the list you want to remove")
    print_menu(choices_list)
    selected_options = []
    while True:
        user_input = input("Enter the number(s) of the option you would like to select (or, 'done' if you are finished with the selection interface): ") 
        if user_input.lower() == 'done':
            break
        try:
            option_index = int(user_input) - 1
            if 0 <= option_index < len(choices_list):
              selected_options.append(choices_list[option_index])
            else:
              print("Invalid option number. Try again.")
        except ValueError:
            print("Invalid input. Enter a number or 'done'.")
    if selected_options:
        print("You selected the following options:")
        for option in selected_options:
            print(option)
    else:
        print("No option selected")

task_list = ["Vacuum", "Clean Windows", "Spray Poison"]
def menu():
    print("To-Do-List Menu")
    print("1. Add a Task")
    print("2. View Tasks")
    print("3. Remove Tasks")
    print("4. Complete Tasks")
    user_input1 = input("Please enter 1-4 to select a menu choice: ")
    if(user_input1 == "1"):
        task_input = input("Please enter task description: ")
        task_list.append(task_input)
        print(task_list)
        menu()
    elif(user_input1 == "2"):
        print(task_list)
        menu()
    elif(user_input1 == "3"):
        input("What would you like to remove?: ")
        for task in task_list:
            print(task)  

menu()

# user_input1 = input("Would you like to add a new task?")
# if(user_input1 == "yes"):
#     task_input = input("What would you like to add?")
# elif(user_input1 == "no"):
#     menu_input1 = input("Okay, here are your listed tasks")
# else:
#     print("Unrecognized input. Please enter yes, or no")
