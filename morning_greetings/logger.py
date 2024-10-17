import datetime
from typing import Dict


def log_message(contact: Dict[str, str], message: str) -> None:
    """
    Logs the sent message with a timestamp to a log file.

    Args:
        contact (Dict[str, str]): The contact information of the friend (name, contact info, etc.).
        message (str): The message that was sent.
    """
    with open("message_log.txt", "a") as log_file:
        log_file.write(f"{datetime.datetime.now()} - Sent to {contact['name']}: {message}\n")
