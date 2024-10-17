from typing import List, Dict


class ContactsManager:
    """
    A class to manage a list of contacts, allowing adding, removing, and retrieving contacts.
    Each contact contains a name, email, and preferred greeting time.
    """

    def __init__(self) -> None:
        """
        Initialize the contact manager with an optional default contact list.
        """
        self.contacts: List[Dict[str, str]] = [
            {"name": "Alice", "email": "alice@example.com", "preferred_time": "08:00 AM"},
            {"name": "Bob", "email": "bob@example.com", "preferred_time": "09:00 AM"},
            {"name": "Charlie", "email": "charlie@example.com", "preferred_time": "07:30 AM"}
        ]

    def add_contact(self, name: str, email: str, preferred_time: str = "08:00 AM") -> None:
        """
        Add a new contact to the contact list.

        Args:
            name (str): The name of the contact.
            email (str): The email of the contact.
            preferred_time (str, optional): The preferred time for greetings. Defaults to "08:00 AM".
        """
        contact = {
            'name': name,
            'email': email,
            'preferred_time': preferred_time
        }
        self.contacts.append(contact)

    def remove_contact(self, name: str) -> None:
        """
        Remove a contact from the contact list by name.

        Args:
            name (str): The name of the contact to be removed.
        """
        self.contacts = [c for c in self.contacts if c['name'] != name]

    def get_contacts(self) -> List[Dict[str, str]]:
        """
        Retrieve the current contact list.

        Returns:
            List[Dict[str, str]]: A list of contacts, each containing name, email, and preferred_time.
        """
        return self.contacts

    def list_contacts(self) -> None:
        """
        Print out all contacts in the contact list.
        """
        for contact in self.contacts:
            print(f"Name: {contact['name']}, Email: {contact['email']}, Preferred Time: {contact['preferred_time']}")
