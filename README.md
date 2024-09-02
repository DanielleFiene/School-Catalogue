# School-Catalogue

# School Management System

This project is a Python-based object-oriented system for representing schools, including different types such as primary schools and high schools. It demonstrates class inheritance, encapsulation, and polymorphism, providing a basic framework for managing school information such as name, level, number of students, and specific attributes like pickup policies for primary schools and sports teams for high schools.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Class Structure](#class-structure)
  - [School](#school)
  - [PrimarySchool](#primaryschool)
  - [HighSchool](#highschool)
- [Example Usage](#example-usage)
- [How to Run](#how-to-run)
- [Learning Outcomes](#learning-outcomes)
- [Contributing](#contributing)
- [License](#license)

## Project Overview

The system is designed to manage and represent different types of schools. The base `School` class provides common attributes and methods, while specialized classes `PrimarySchool` and `HighSchool` extend this base class to add unique features.

## Features

- **Encapsulation**: Manage school details with getter and setter methods.
- **Inheritance**: Specialized classes `PrimarySchool` and `HighSchool` inherit from the `School` class.
- **Polymorphism**: The `__repr__` method is overridden in each subclass to provide specific string representations of each type of school.
- **Input Validation**: Ensures that only valid data types are accepted, particularly for the number of students.

## Class Structure

### `School`

The `School` class is the base class that represents a general school. It includes:
- **Attributes**:
  - `name`: The name of the school.
  - `level`: The level of the school (e.g., primary, high).
  - `numberOfStudents`: The total number of students enrolled.
- **Methods**:
  - `get_name()`: Returns the name of the school.
  - `get_level()`: Returns the level of the school.
  - `get_numberOfStudents()`: Returns the number of students.
  - `set_numberOfStudents(newNumberOfStudents)`: Updates the number of students if the input is valid.
  - `__repr__()`: Returns a string representation of the school.

### `PrimarySchool`

The `PrimarySchool` class inherits from `School` and represents a primary school. It adds:
- **Attributes**:
  - `pickupPolicy`: The pickup policy for students.
- **Methods**:
  - `get_pickupPolicy()`: Returns the pickup policy.
  - `__repr__()`: Returns a string representation including the pickup policy.

### `HighSchool`

The `HighSchool` class inherits from `School` and represents a high school. It adds:
- **Attributes**:
  - `sportsTeams`: A list of sports teams available at the school.
- **Methods**:
  - `get_sportsTeams()`: Returns the list of sports teams.
  - `__repr__()`: Returns a string representation including the sports teams.

## Example Usage

Here is an example of how the classes can be used:

```python
# Creating a PrimarySchool instance
b = PrimarySchool("Codecademy", 300, "Pickup Allowed")
print(b.get_pickupPolicy())  # Outputs: Pickup Allowed
print(b)  # Outputs: A primary school named Codecademy which currently has 300 students. The pickup policy is Pickup Allowed.

# Creating a HighSchool instance
c = HighSchool('Oscar Romero', 4850, ['Golden Eagles', 'Horse Girls'])
print(c.get_sportsTeams())  # Outputs: ['Golden Eagles', 'Horse Girls']
print(c)  # Outputs: A high school named Oscar Romero which currently has 4850 students. The sports teams are: Golden Eagles, Horse Girls.
```

## How to Run

1. Clone this repository to your local machine.
2. Ensure you have Python installed.
3. Navigate to the directory containing the script.
4. Run the script:

   ```bash
   python school_management_system.py
   ```

5. Observe the output in the terminal, which will demonstrate the class functionality.

## Learning Outcomes

By studying and running this code, you'll gain insights into:
- **Object-Oriented Programming (OOP)**: Understanding class structures, inheritance, and encapsulation.
- **Python Programming**: How to build and extend classes in Python.
- **Polymorphism**: Implementing and overriding methods to provide specific behavior in subclasses.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have suggestions for improvements, additional features, or bug fixes.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

