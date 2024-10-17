import re


class Contact:
    """
    A class to represent an individual contact.

    Attributes:
        name (str): The name of the contact.
        email (str): The contact's email address.
        preferred_time (str): The contact's preferred greeting time.
    """

    def __init__(self, name: str, email: str, preferred_time: str = "08:00 AM") -> None:
        if not name:
            raise ValueError("Contact name cannot be empty.")
        if not self.is_valid_email(email):
            raise ValueError("Invalid email address.")
        
        self.name = name
        self.email = email
        self.preferred_time = preferred_time

    def __repr__(self) -> str:
        return f"Contact(name={self.name}, email={self.email}, preferred_time={self.preferred_time})"

    def __eq__(self, other: object) -> bool:
        """Override equality operator to compare Contact objects."""
        if isinstance(other, Contact):
            return (self.name == other.name and 
                    self.email == other.email and 
                    self.preferred_time == other.preferred_time)
        return False

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Validates the email format.
        
        Args:
            email (str): Email to validate.
        
        Returns:
            bool: True if valid, False otherwise.
        """
        pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        return re.match(pattern, email) is not None
