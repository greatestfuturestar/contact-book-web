
import json
import os

def load_contacts():
    filename = "contacts.json"

    if not os.path.exists(filename):

        return []
    with open(filename, "r") as file:

        return json.load(file)

def save_contacts(contacts):

    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

    return contacts
    
def add_contact(contacts, name, phone_number, email, address):

    new_contacts = {"name": name, "phone_number": phone_number, "email": email, "address": address}

    contacts.append(new_contacts)

    return contacts

def remove_contact(contacts, user_remove):
    for index, contact in enumerate(contacts):
        if user_remove == contact["name"] or user_remove == contact["phone_number"] or user_remove  == contact["email"] or user_remove == contact["address"]:

            contacts.pop(index)

    return contacts    

def edit_contact(contacts, contactName, newContact):
    for index, contact in enumerate(contacts):
        if contactName == contact["name"]:
            contacts[index]["name"] = newContact

        elif contactName == contact["phone_number"]:
            contacts[index]["phone_number"] = newContact

        elif contactName  == contact["email"]:
            contacts[index]["email"] = newContact

        elif contactName == contact["address"]:
            contacts[index]["address"] = newContact


    return contacts

def search_contact(contacts, user_search):
    for contact in contacts:
        if user_search == contact["name"] or user_search == contact["phone_number"] or user_search  == contact["email"] or user_search == contact["address"]:
  
            return contact

    return contacts

def view_contacts(contacts):
    for contact in contacts:
        print(f"Name: {contact["name"]}")
        print(f"Phone number: {contact["phone_number"]}")
        print(f"email: {contact["email"]}")
        print(f"Home address: {contact["address"]}")

    return contacts


