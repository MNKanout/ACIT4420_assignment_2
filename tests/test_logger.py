import unittest
from morning_greetings.logger import log_message
import os


class TestLogger(unittest.TestCase):
    
    def test_log_message(self):
        """Test logging a message."""
        contact = {"name": "Diana", "email": "diana@example.com"}
        message = "Good Morning, Diana!"
        
        try:
            log_message(contact, message)
            # Check if the log file exists and has content
            self.assertTrue(os.path.exists("message_log.txt"))
            with open("message_log.txt", "r") as f:
                content = f.read()
                self.assertIn("Diana", content)  # Ensure the name is logged
        except IOError:
            self.fail("log_message raised IOError unexpectedly!")


if __name__ == '__main__':
    unittest.main()
