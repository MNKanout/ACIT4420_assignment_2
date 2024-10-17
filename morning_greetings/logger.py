import datetime

def log_message(contact: dict, message: str) -> None:
    """
    Logs the sent message to a log file.
    
    Args:
        contact (dict): The contact information.
        message (str): The message that was sent.
        
    Raises:
        IOError: If there is an issue writing to the log file.
    """
    try:
        with open("message_log.txt", "a") as log_file:
            log_file.write(f"{datetime.datetime.now()} - Sent to {contact['name']}: {message}\n")
    except IOError as e:
        raise IOError(f"Failed to write to log file: {e}")
