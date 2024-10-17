import unittest
from morning_greetings.message_sender import send_message


class TestMessageSender(unittest.TestCase):
    
    def test_send_message(self):
        """
        Test if sending a message correctly prints the expected output.
        """
        email = "test@example.com"
        message = "Good Morning, Test! Have a great day!"
        
        with self.assertLogs() as captured:
            send_message(email, message)
            self.assertIn(f"Sending message to {email}: {message}", captured.output)

    def test_send_message_missing_email(self):
        """
        Test if a missing email raises a ValueError.
        """
        with self.assertRaises(ValueError):
            send_message("", "Test message")


if __name__ == '__main__':
    unittest.main()
