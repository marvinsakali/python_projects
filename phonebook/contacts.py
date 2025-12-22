def add_contacts(contacts, names):
    name = input("Enter Name of contact you want to add: ")
    phone = input("Enter the phone number: ")
    contact = {
        "name": name,
        "phone": phone
    }
    contacts.append(contact)
    names.add(name)

def view_contacts(contacts):
    if not contacts:
        print("No contacts added")
    else:
        for index, contact in enumerate(contacts):
            print(f"{index + 1}. {contact['name']} -> {contact['phone']}")
    

def delete_contacts(contacts):
    name = input("Enter the number you want to delete:")
    if name in contacts:
        del contacts[name]
    else: 
        print(f"{name} not in contact list")

def search_contacts(contacts):
    search = input("Enter contact you want to search: ")
    found = False
    for index, contact in enumerate(contacts, start = 1):
        if  contact["name"] == search :
            print(f"{index}. {contact['name']} {contact['phone']}")
        found = True
    if not found:
        print(f"{search} Not found")
    