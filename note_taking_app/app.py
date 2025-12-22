
def add_note():
    notes = input("Add notes: ").strip().title()
    
    try:
        with open("note.txt", 'a') as file:
            file.write(notes + "\n")
        print("Note added successfully.")
    except TypeError:
        print("add an argument in the .write()")

def view_notes():
    try:
        with open("note.txt", 'r') as file:
            notes = file.readlines()
            if notes: 
                print("These are your notes")
                for idx, note in enumerate(notes, start = 1):
                    print(f"{idx}. {note}")
            else:
                print("There are no notes")
    except FileNotFoundError:
        print("That file does not exist")
    

def delete_notes():
    view_notes()
    note_num = int(input("Enter the note number to be deleted: "))
    try:
        with open("note.txt", "r") as file:
            notes = file.readlines()

        if 0 < note_num <= len(notes):
            removed = notes.pop(note_num -  1)
            print("Not was deleted")
            with open ("note.txt", "w") as file:
                file.writelines(notes)

        else: 
            print("Invalid note number")
    except ValueError:
        print("Please enter a valid Number")

    except FileNotFoundError:
        print("File not found")

def main():
    print("\n -Note Taking App- ")   
    

   
    while True:
        print(""" 
    1. Add Note     
    2. View Notes   
    3. Delete Notes 
    4. Exit App
 """)
        choice = input("Enter your choice: ")
              
    
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            delete_notes()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try Again!")

if __name__ == "__main__":
    main()