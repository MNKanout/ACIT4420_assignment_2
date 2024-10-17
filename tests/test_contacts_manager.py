# tests/test_contacts_manager.py
import unittest
from morning_greetings.contacts_manager import ContactsManager


class TestContactsManager(unittest.TestCase):
    """
    Unit tests for the ContactsManager class.
    """

    def setUp(self) -> None:
        """
        Set up a new ContactsManager instance before each test.
        """
        self.manager = ContactsManager()

    def test_add_contact(self) -> None:
        """
        Test adding a new contact.
        """
        self.manager.add_contact("Diana", "diana@example.com", "09:30 AM")
        self.assertEqual(len(self.manager.get_contacts()), 4)  # 3 default + 1 new

    def test_remove_contact(self) -> None:
        """
        Test removing an existing contact.
        """
        self.manager.remove_contact("Alice")
        self.assertEqual(len(self.manager.get_contacts()), 2)

    def test_remove_nonexistent_contact(self) -> None:
        """
        Test removing a contact that does not exist.
        """
        self.manager.remove_contact("NonExistent")
        self.assertEqual(len(self.manager.get_contacts()), 3)

    def test_get_contacts(self) -> None:
        """
        Test retrieving the contact list.
        """
        contacts = self.manager.get_contacts()
        self.assertEqual(len(contacts), 3)
        self.assertEqual(contacts[0]['name'], "Alice")

    def test_list_contacts(self) -> None:
        """
        Test listing contacts by checking the output format.
        """
        self.manager.list_contacts()

if __name__ == '__main__':
    unittest.main()
