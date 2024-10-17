def generate_message(name: str) -> str:
    """
    Generates a personalized "Good Morning" message for a friend.

    Args:
        name (str): The name of the friend.

    Returns:
        str: A personalized "Good Morning" message.
    """
    return f"Good Morning, {name}! Have a great day!"


def send_message(contact_info: str, message: str) -> None:
    """
    Simulates sending a message to a contact.

    Args:
        contact_info (str): The contact information of the recipient (e.g., email).
        message (str): The message to send.

    Raises:
        ValueError: If the contact information is missing.
    """
    if not contact_info:
        raise ValueError("Contact information is missing.")
    
    # Simulating message sending (for real-world use, this can be replaced with actual sending logic)
    print(f"Sending message to {contact_info}: {message}")
