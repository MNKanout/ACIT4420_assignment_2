# contacts.py
from typing import List, Dict


class Contacts:
    """
    Class to manage a list of friends' contact information.

    Attributes:
        contacts (List[Dict[str, str]]): A list of dictionaries holding friends' information.
    """

    def __init__(self) -> None:
        """
        Initializes an empty contact list.
        """
        self.contacts: List[Dict[str, str]] = []

    def add_contact(self, name: str, contact_info: str, preferred_time: str = "08:00 AM") -> None:
        """
        Adds a contact to the list.

        Args:
            name (str): The friend's name.
            contact_info (str): The friend's contact information (e.g., email).
            preferred_time (str, optional): The preferred greeting time. Defaults to "08:00 AM".
        """
        contact = {
            'name': name,
            'contact_info': contact_info,
            'preferred_time': preferred_time
        }
        self.contacts.append(contact)

    def remove_contact(self, name: str) -> None:
        """
        Removes a contact from the list by their name.

        Args:
            name (str): The name of the friend to remove.
        """
        self.contacts = [c for c in self.contacts if c['name'] != name]

    def get_contacts(self) -> List[Dict[str, str]]:
        """
        Retrieves the full list of contacts.

        Returns:
            List[Dict[str, str]]: The list of contacts.
        """
        return self.contacts
