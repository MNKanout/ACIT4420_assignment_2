# tests/test_contacts.py
import unittest
from contacts import Contacts


class TestContacts(unittest.TestCase):
    """
    Unit tests for the Contacts class.
    """

    def setUp(self) -> None:
        """
        Set up a new Contacts instance before each test.
        """
        self.contacts = Contacts()

    def test_add_contact(self) -> None:
        """
        Test adding a new contact.
        """
        self.contacts.add_contact("Alice", "alice@example.com", "08:00 AM")
        self.assertEqual(len(self.contacts.get_contacts()), 1)
        self.assertEqual(self.contacts.get_contacts()[0]['name'], "Alice")

    def test_remove_contact(self) -> None:
        """
        Test removing an existing contact.
        """
        self.contacts.add_contact("Bob", "bob@example.com", "09:00 AM")
        self.contacts.remove_contact("Bob")
        self.assertEqual(len(self.contacts.get_contacts()), 0)

    def test_remove_nonexistent_contact(self) -> None:
        """
        Test removing a contact that does not exist.
        """
        self.contacts.add_contact("Charlie", "charlie@example.com")
        self.contacts.remove_contact("NonExistent")
        self.assertEqual(len(self.contacts.get_contacts()), 1)

    def test_get_contacts(self) -> None:
        """
        Test retrieving contacts.
        """
        self.contacts.add_contact("David", "david@example.com", "07:30 AM")
        self.contacts.add_contact("Eve", "eve@example.com", "08:15 AM")
        contacts_list = self.contacts.get_contacts()
        self.assertEqual(len(contacts_list), 2)
        self.assertEqual(contacts_list[0]['name'], "David")
        self.assertEqual(contacts_list[1]['name'], "Eve")

    def test_contact_initialization(self) -> None:
        """
        Test that the contact list is initialized as empty.
        """
        self.assertEqual(len(self.contacts.get_contacts()), 0)

if __name__ == '__main__':
    unittest.main()
