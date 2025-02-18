# Calculator App

A simple Python-based calculator application that performs basic arithmetic operations like addition, subtraction, multiplication, and division. The program provides a command-line interface where users can interactively perform calculations or quit the app.

## Features

- Perform basic arithmetic operations:
  - Addition
  - Subtraction
  - Multiplication
  - Division
- Continuously perform calculations until the user chooses to quit
- Easy-to-use command-line interface

## Installation

### Prerequisites
- Python 3.x is required to run the app.

### Steps to Install

1. Clone the repository:
   ```bash
   git clone https://github.com/PrajaktaOlekar/Calculator-App.git
   ```

2. Navigate to the project directory:
   ```bash
   cd Calculator-App
   ```

3. You don’t need to install any additional dependencies, as the program only relies on the Python standard library.

## Usage

1. After cloning the repository and navigating to the project directory, you can run the `Calculator-App` by executing the following command:
   ```bash
   python calculator.py
   ```

2. The app will print the following welcome message:
   ```
   -----WELCOME TO CALCULATOR APP-----
   ```

3. The user is prompted with the following options:
   ```
   Enter:
   - 'a' for addition
   - 's' for subtraction
   - 'm' for multiplication
   - 'd' for division
   - 'q' for quit
   ```

4. You can then enter the numbers for the selected operation, and the result will be displayed. The user can perform multiple operations or quit by entering `'q'`.

### Example:

```
-----WELCOME TO CALCULATOR APP-----
Enter:
- 'a' for addition
- 's' for subtraction
- 'm' for multiplication
- 'd' for division
- 'q' for quit

YOUR_CHOICE: a
Enter the value of a: 5
Enter the value of b: 3
Addition is: 8
Enter:
- 'a' for addition
- 's' for subtraction
- 'm' for multiplication
- 'd' for division
- 'q' for quit

YOUR_CHOICE: m
Enter the value of a: 4
Enter the value of b: 2
Multiplication is: 8
Enter:
- 'a' for addition
- 's' for subtraction
- 'm' for multiplication
- 'd' for division
- 'q' for quit

YOUR_CHOICE: q
-----THANK YOU FOR USING OUR APP-----
```

## Code Structure

- **calculator.py**: The main script that contains the logic for the calculator app.
  - **`Calculator` class**: Contains methods for handling operations (`add`, `subtract`, `multiply`, `divide`) and user input.
  - **`main` function**: Starts the program and handles the flow of user interaction.

## Contributing

If you'd like to contribute to this project, feel free to fork the repository and create a pull request. If you have any suggestions or issues, please create an issue in the Issues section.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

