import unittest
from morning_greetings.message_sender import send_message


class TestMessageSender(unittest.TestCase):

    def test_send_message(self):
        """Test sending a valid message."""
        try:
            send_message("diana@example.com", "Hello Diana!")
            self.assertTrue(True)  # If no exception is raised, the test passes.
        except ValueError:
            self.fail("send_message raised ValueError unexpectedly!")

    def test_empty_email(self):
        """Test sending a message with an empty email raises an error."""
        with self.assertRaises(ValueError) as context:
            send_message("", "Hello Diana!")
        self.assertEqual(str(context.exception), "Email address is missing.")

    def test_empty_message(self):
        """Test sending an empty message raises an error."""
        with self.assertRaises(ValueError) as context:
            send_message("diana@example.com", "")
        self.assertEqual(str(context.exception), "Message cannot be empty.")


if __name__ == '__main__':
    unittest.main()
