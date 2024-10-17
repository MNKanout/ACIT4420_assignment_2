import unittest
from message_handler import generate_message, send_message


class TestMessageHandler(unittest.TestCase):
    """
    Unit tests for the Message Handler module.
    """

    def test_generate_message(self) -> None:
        """
        Test generating a personalized message.
        """
        message = generate_message("TestUser")
        self.assertEqual(message, "Good Morning, TestUser! Have a great day!")

    def test_send_message_valid(self) -> None:
        """
        Test sending a message with valid contact info.
        """
        try:
            send_message("testuser@example.com", "Hello!")
            # If it doesn't raise an error, the test passes
        except ValueError:
            self.fail("send_message raised ValueError unexpectedly!")

    def test_send_message_invalid(self) -> None:
        """
        Test sending a message with missing contact info.
        """
        with self.assertRaises(ValueError):
            send_message("", "Hello!")


if __name__ == '__main__':
    unittest.main()
