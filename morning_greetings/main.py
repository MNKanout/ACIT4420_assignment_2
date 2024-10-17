from .contacts_manager import ContactsManager
from .message_generator import generate_message
from .message_sender import send_message
from .logger import log_message


def main() -> None:
    """
    Main function to run the automation process.
    """
    # Initialize the contacts manager and retrieve the contact list
    manager = ContactsManager()
    contacts = manager.get_contacts()

    # Iterate over each contact, generate a message, send it, and log it
    for contact in contacts:
        name = contact.name
        email = contact.email
        message = generate_message(name)
        
        try:
            send_message(email, message)   # Simulate sending message
            log_message({"name": name, "email": email}, message)  # Log the message sent
        except ValueError as e:
            print(f"Failed to send message to {name}: {e}")
            

if __name__ == "__main__":
    main()
