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
