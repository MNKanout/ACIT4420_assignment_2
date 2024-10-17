def generate_message(name: str) -> str:
    """
    Generates a personalized 'Good Morning' message.
    
    Args:
        name (str): The name of the recipient.
        
    Returns:
        str: A personalized greeting message.
        
    Raises:
        ValueError: If the name is empty.
    """
    if not name:
        raise ValueError("Name cannot be empty.")
    return f"Good Morning, {name}! Have a great day!"
