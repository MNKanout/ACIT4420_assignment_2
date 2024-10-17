class Contact:
    """
    A class to represent an individual contact.
    
    Attributes:
        name (str): The name of the contact.
        email (str): The contact's email address.
        preferred_time (str): The contact's preferred greeting time.
    """
    
    def __init__(self, name: str, email: str, preferred_time: str = "08:00 AM") -> None:
        self.name = name
        self.email = email
        self.preferred_time = preferred_time

    def __repr__(self) -> str:
        return f"Contact(name={self.name}, email={self.email}, preferred_time={self.preferred_time})"
