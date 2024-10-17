import unittest
from morning_greetings.contacts import Contact


class TestContact(unittest.TestCase):
    
    def test_contact_creation(self):
        """Test creating a contact instance."""
        contact = Contact("Diana", "diana@example.com", "09:00 AM")
        self.assertEqual(contact.name, "Diana")
        self.assertEqual(contact.email, "diana@example.com")
        self.assertEqual(contact.preferred_time, "09:00 AM")

    def test_contact_default_preferred_time(self):
        """Test creating a contact with the default preferred time."""
        contact = Contact("Eve", "eve@example.com")
        self.assertEqual(contact.preferred_time, "08:00 AM")

    def test_invalid_name(self):
        """Test that creating a contact with an empty name raises an error."""
        with self.assertRaises(ValueError) as context:
            Contact("", "test@example.com")
        self.assertEqual(str(context.exception), "Contact name cannot be empty.")

    def test_invalid_email(self):
        """Test that creating a contact with an invalid email raises an error."""
        with self.assertRaises(ValueError) as context:
            Contact("Eve", "invalid-email")
        self.assertEqual(str(context.exception), "Invalid email address.")


if __name__ == '__main__':
    unittest.main()
