import unittest
from morning_greetings.message_generator import generate_message

class TestMessageGenerator(unittest.TestCase):
    
    def test_generate_message(self):
        """
        Test if the message generator correctly creates a personalized message.
        """
        name = "Alice"
        expected_message = "Good Morning, Alice! Have a great day!"
        self.assertEqual(generate_message(name), expected_message)

if __name__ == '__main__':
    unittest.main()
