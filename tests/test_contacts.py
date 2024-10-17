import unittest
from morning_greetings.contacts import Contact


class TestContact(unittest.TestCase):
    
    def test_contact_creation(self):
        """
        Test creating a contact instance.
        """
        contact = Contact("Diana", "diana@example.com", "09:00 AM")
        self.assertEqual(contact.name, "Diana")
        self.assertEqual(contact.email, "diana@example.com")
        self.assertEqual(contact.preferred_time, "09:00 AM")

    def test_contact_default_preferred_time(self):
        """
        Test creating a contact with the default preferred time.
        """
        contact = Contact("Eve", "eve@example.com")
        self.assertEqual(contact.preferred_time, "08:00 AM")


if __name__ == '__main__':
    unittest.main()
