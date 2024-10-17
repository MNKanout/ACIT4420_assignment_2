import unittest
from morning_greetings.contacts_manager import ContactsManager
from morning_greetings.contacts import Contact


class TestContactsManager(unittest.TestCase):
    
    def setUp(self):
        self.manager = ContactsManager()

    def test_add_contact(self):
        """
        Test if a contact is added correctly.
        """
        self.manager.add_contact("Diana", "diana@example.com", "09:00 AM")
        contacts = self.manager.get_contacts()
        self.assertIn(Contact("Diana", "diana@example.com", "09:00 AM"), contacts)

    def test_remove_contact(self):
        """
        Test if a contact is removed correctly.
        """
        self.manager.remove_contact("Alice")
        contacts = self.manager.get_contacts()
        self.assertNotIn(Contact("Alice", "alice@example.com", "08:00 AM"), contacts)

    def test_get_contacts(self):
        """
        Test retrieving all contacts.
        """
        contacts = self.manager.get_contacts()
        self.assertEqual(len(contacts), 3)  # By default, 3 contacts are initialized


if __name__ == '__main__':
    unittest.main()
