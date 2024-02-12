# AirBnB Clone Project

This project is a clone of the popular accommodation rental platform AirBnB. It aims to replicate some of the core functionalities of AirBnB, allowing users to list properties for rent, search for properties, make bookings, and manage their bookings.

## Command Interpreter

The command interpreter serves as the interface for interacting with the AirBnB clone system. It allows users to perform various actions such as creating listings, searching for properties, making bookings, and managing bookings.

### How to Start the Command Interpreter

To start the command interpreter, follow these steps:

1. Clone the repository to your local machine:
   ```
   git clone https://github.com/yourusername/AirBnB-Clone.git
   ```

2. Navigate to the project directory:
   ```
   cd AirBnB-Clone
   ```

3. Run the command interpreter script:
   ```
   python3 console.py
   ```

### How to Use the Command Interpreter

Once the command interpreter is running, you can enter commands to interact with the AirBnB clone system. The following are some of the available commands:

- `create <class>`: Create a new instance of the specified class (e.g., `create User`).
- `show <class> <id>`: Show details of the instance with the specified ID (e.g., `show User 123`).
- `update <class> <id> <attribute> <value>`: Update the attribute of the specified instance (e.g., `update User 123 name "John Doe"`).
- `destroy <class> <id>`: Delete the instance with the specified ID (e.g., `destroy User 123`).
- `all <class>`: Show all instances of the specified class (e.g., `all User`).
- `quit`: Exit the command interpreter.

### Examples

Here are some examples of how to use the command interpreter:

1. Create a new user:
   ```
   (hbnb) create User
   ```

2. Show details of a user:
   ```
   (hbnb) show User 123
   ```

3. Update the name of a user:
   ```
   (hbnb) update User 123 name "John Doe"
   ```

4. Delete a user:
   ```
   (hbnb) destroy User 123
   ```

5. Show all users:
   ```
   (hbnb) all User
   ```

6. Exit the command interpreter:
   ```
   (hbnb) quit
   ```
