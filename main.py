# main.py
from morning_greetings.contacts_manager import ContactsManager
from morning_greetings.message_handler import generate_message, send_message
from morning_greetings.logger import log_message


def main() -> None:
    """
    Main function to automate the sending of personalized 'Good Morning' messages to all contacts.
    
    - Fetches the contact list.
    - Generates personalized messages for each contact.
    - Simulates sending each message.
    - Logs the message details.
    """
    # Instantiate the contacts manager
    manager = ContactsManager()
    
    # Get the list of contacts
    contacts = manager.get_contacts()
    
    if not contacts:
        print("No contacts found.")
        return
    
    # Iterate over each contact
    for contact in contacts:
        # Generate personalized message
        message = generate_message(contact['name'])
        
        # Simulate sending the message
        send_message(contact['email'], message)
        
        # Log the message
        log_message(contact, message)


if __name__ == "__main__":
    main()
