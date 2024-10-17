def send_message(email: str, message: str) -> None:
    """
    Simulates sending a message to a contact.
    
    Args:
        email (str): The email address of the contact.
        message (str): The personalized message to be sent.
    
    Raises:
        ValueError: If the email is empty or invalid.
    """
    if not email:
        raise ValueError("Email address is missing")
    
    # Simulate sending the message
    print(f"Sending message to {email}: {message}")
