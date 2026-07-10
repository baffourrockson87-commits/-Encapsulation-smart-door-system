# -Encapsulation-smart-door-system
# Smart Door Access System for UMaT


## Assignment Overview

This project implements a **Smart Door Access System** for the University of Mines and Technology (UMaT). The system demonstrates the concept of **encapsulation** in Python by protecting a staff member's access code from direct modification.

The project uses Python's **@property** decorator to control access to a private attribute instead of using traditional getter and setter methods.

## Objectives

The program is designed to:

- Create a `Staff` class.
- Store the staff member's name as a public attribute.
- Store the access code as a private attribute.
- Allow authorized users to view the access code.
- Validate the access code before updating it.
- Display staff information.
- Demonstrate encapsulation using the `@property` decorator.

## Features

- Public attribute: `s_name`
- Private attribute: `__access_code`
- Property method for viewing the access code
- Property setter for updating the access code
- Validation to ensure the access code has at least six (6) characters
- Method to display staff information

## Concepts Demonstrated

- Classes and Objects
- Constructors (`__init__`)
- Encapsulation
- Private Attributes
- `@property` Decorator
- Property Setters
- Object-Oriented Programming (OOP)

## Project Structure

```
Smart-Door-Access-System/
│
├── smart_door_access.py
└── README.md
```

```bash
python smart_door_access.py
```

## Expected Output

The program will:

- Display staff information.
- Allow viewing of the access code.
- Update the access code if it meets the required length.
- Reject invalid access codes that are shorter than six characters.

## Conclusion

This project demonstrates the use of encapsulation in Python through private attributes and the `@property` decorator. It provides a simple and secure approach to managing staff access codes in a smart door access system.
