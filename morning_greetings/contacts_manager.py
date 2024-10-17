from typing import List
from morning_greetings.contacts import Contact


class ContactsManager:
    """
    A class to manage a list of contacts.
    
    Methods:
        add_contact(name, email, preferred_time): Adds a contact to the list.
        remove_contact(name): Removes a contact by name.
        get_contacts(): Retrieves all contacts.
    """
    
    def __init__(self) -> None:
        self.contacts: List[Contact] = [
            Contact("Alice", "alice@example.com", "08:00 AM"),
            Contact("Bob", "bob@example.com", "09:00 AM"),
            Contact("Charlie", "charlie@example.com", "07:30 AM")
        ]

    def add_contact(self, name: str, email: str, preferred_time: str = "08:00 AM") -> None:
        """
        Adds a contact to the contacts list.
        
        Args:
            name (str): The contact's name.
            email (str): The contact's email.
            preferred_time (str): The preferred greeting time.
        """
        contact = Contact(name, email, preferred_time)
        self.contacts.append(contact)

    def remove_contact(self, name: str) -> None:
        """
        Removes a contact from the list by name.
        
        Args:
            name (str): The name of the contact to remove.
        """
        self.contacts = [c for c in self.contacts if c.name != name]

    def get_contacts(self) -> List[Contact]:
        """
        Returns the list of contacts.
        
        Returns:
            List[Contact]: The list of contacts.
        """
        return self.contacts
