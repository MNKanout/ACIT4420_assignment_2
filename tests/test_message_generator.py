import unittest
from morning_greetings.message_generator import generate_message


class TestMessageGenerator(unittest.TestCase):
    
    def test_generate_message(self):
        """Test generating a valid message."""
        message = generate_message("Diana")
        self.assertEqual(message, "Good Morning, Diana! Have a great day!")

    def test_empty_name(self):
        """Test generating a message with an empty name raises an error."""
        with self.assertRaises(ValueError) as context:
            generate_message("")
        self.assertEqual(str(context.exception), "Name cannot be empty.")


if __name__ == '__main__':
    unittest.main()
