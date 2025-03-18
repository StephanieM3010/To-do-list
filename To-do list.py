tasks = []

def addTask():
    task = input("Please enter  task: ")
    tasks.append(task)
    print(f"{task} added successfully")


def showTasks():
    if not tasks:
        print("Your to-do list is empty.")
    else:
        print("Current tasks:")
        for index, task in enumerate(tasks):
            print(f"Task {index}. {task}")
            

def deleteTask():
   showTasks()
   task_to_delete = int(input("Enter the no. of the task you want to delete: "))
   if task_to_delete >=0 and task_to_delete < len(tasks):
          tasks.pop(task_to_delete)
          print(f"{task_to_delete} has been removed.")
   else:
           print(f"{task_to_delete} was not found.")
    
if __name__ == "__main__":
    print("STEPHANIE'S TO DO LIST:")
    while True:
        print("/n Select one of the following options: ")
        print("-------------------------------------")
        print("1. Add new task")
        print("2. Delete task")
        print("3. Show tasks")
        print("4. Quit")

        choice = input("Enter your choice: ")
        
        if(choice == "1" ):
            addTask()
        elif(choice == "2"):
            deleteTask()
        elif(choice == "3"):
            showTasks()
        elif(choice == "4"):
            break
        else:
            print("Input is invalid. Try again.")
             
        
        
