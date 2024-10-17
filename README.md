# Morning Greetings Package

The **Morning Greetings** package automates the process of sending personalized "Good Morning" messages to a list of friends. This package is designed to manage contacts, generate customized messages, and simulate sending those messages.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Running Tests](#running-tests)
- [Experience Report](#experience-report)

## Installation

To install the `morning_greetings` package locally, follow these steps:

1. **Clone the repository:**

   ```bash
   git clone https://github.com/MNKanout/ACIT4420_assignment_2
   cd morning_greetings
   ```

2. **Install the package using pip:**

   You can install the package in editable mode (recommended) so you can modify the source code if needed.

   ```bash
   pip install -e .
   ```

### Dependencies:

This package has no external dependencies other than the standard Python library.

## Usage

To use the morning_greetings package, follow these steps:

### Add Contacts

You can manage contacts using the `ContactsManager` class. Here’s an example of how to add a new contact:

```python
from morning_greetings.contacts_manager import ContactsManager

contacts_manager = ContactsManager()
contacts_manager.add_contact("Diana", "diana@example.com", "09:00 AM")
```

### Send Personalized Messages

You can use the `message_generator` and `message_sender` modules to generate and send messages:

```python
from morning_greetings.message_generator import generate_message
from morning_greetings.message_sender import send_message

message = generate_message("Diana")
send_message("diana@example.com", message)
```

### Logging Messages

Messages sent are automatically logged in `message_log.txt`.

### Running the Automation Task

To run the complete automation process, execute the `main.py` script:

```bash
python main.py
```

## Running Tests

To ensure everything is working correctly, you can run the unit tests provided in the tests directory. Use the following command:

```bash
python -m unittest discover -s tests -p "*.py"
```

Alternatively, you can use the `test.py` script to run all tests:

```bash
python test.py
```

## Experience Report

### Challenges Faced

- **Error Handling:** Implementing error handling for each module was crucial but challenging at first. Ensuring meaningful error messages for invalid inputs took some time to consider.

- **Module Integration:** Merging different modules and ensuring they worked cohesively required careful planning, particularly in managing the contacts and sending messages.

- **Testing:** Writing unit tests to cover all possible scenarios (especially error scenarios) helped reinforce understanding of the modules' functionalities but required extensive attention to detail to ensure all edge cases were considered.
