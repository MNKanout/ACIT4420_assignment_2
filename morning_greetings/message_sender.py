def send_message(email: str, message: str) -> None:
    """
    Simulates sending a message to the specified email address.
    
    Args:
        email (str): The recipient's email address.
        message (str): The message to send.
        
    Raises:
        ValueError: If the email address or message is invalid.
    """
    if not email:
        raise ValueError("Email address is missing.")
    if not message:
        raise ValueError("Message cannot be empty.")

    # Simulate sending a message (replace this with actual email sending logic if needed)
    print(f"Sending message to {email}: {message}")
