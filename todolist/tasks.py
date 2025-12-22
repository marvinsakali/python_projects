def add_tasks(tasks):
    task = input("Enter the task you want to add: ")
    tasks.append(task)
    print(f"{task} added successfully")

def view_tasks(tasks):
    
    if len(tasks) == 0:
        print("No tasks!")
    else:
        print("Here are our tasks for the day")
        for i in range(len(tasks)):
            print(f"{i + 1}. {tasks[i]}") 


def complete_tasks(tasks):
    view_tasks(tasks)

    
    if len(tasks) == 0:
        return 
        
    completed = int(input("Enter the task you want marked as completed: "))

    if 1 <= completed  <= (len(tasks)):
        tasks[ completed - 1] += " --> COMPLETED"
        print(f" {completed} marked as completed")

    else:
        print("Invalid task selected")



def delete_tasks(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    num = int(input("Enter the task you want to delete: "))

    if 1 <= num <= len(tasks):
        deleted = tasks.pop(num-1)

        print(f"{deleted} was deleted")

    else: 
        print("Invalid choice")
