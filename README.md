# Savings Tracker

# Project Overview

The Savings Tracker is a Python-based financial tracking program that calculates a user’s total savings over 12 months. The system collects monthly savings data, computes the annual total, and optionally adds a yearly bonus.
This project demonstrates the application of core programming concepts including iteration, conditional logic, user input handling, and data computation.

# Updated Feature List

Collects 12 months of savings input using a loop
Computes total annual savings
Allows user to indicate whether a yearly bonus was received
Adds bonus amount to total savings if applicable
Handles invalid bonus responses using conditional checks
Displays final adjusted savings

# Technologies Used

Python 3.13.7
Chosen for its readability, simplicity, and suitability for beginner-to-intermediate programming projects. Python supports clear syntax for loops and conditionals, making it ideal for financial computation tasks.

# Detailed Methodology

## Core Feature Implementation

### 1. Monthly Savings Collection
A for loop iterates from 1 to 12, prompting the user to input savings for each month. Each input is converted into a float and accumulated into a running total variable (tts).

### 2. Bonus Feature
A conditional statement checks whether the user received a bonus.
If "Yes", the bonus amount is added to the total savings.
If "No", no changes are made.
If another response is given, the program defaults to assuming no bonus.

### 3. Final Computation
After all inputs are processed, the program outputs the final savings total.

# File Structure

#### --> savings_tracker.py

#### --> README.md

#### --> CHANGELOG.md

The structure is intentionally minimal to maintain clarity and organization.

# Installation and Execution Instructions

1. Install Python 3.13.7 or newer.
2. Clone this repository or download the source file.
3. Open terminal/command prompt.
4. Navigate to the project directory.
5. Run:
python savings_tracker.py

# Current Project Status

Version 1.2.0 — Emergency Withdrawal feature implemented.
Further updates may include stronger input validation and enhanced financial features.

# Programming and Computing Ethics

This project follows responsible programming practices aligned with the ACM Code of Ethics (Association for Computing Machinery, 2018).

## Ethical considerations include:

### Respect for Intellectual Property: All code in this repository was written by the contributors. No external code was copied without attribution.
### User Privacy: The program does not collect, store, or transmit user financial data. All input remains temporary during execution.
### Accessibility: The interface uses clear prompts and straightforward instructions to ensure usability for beginner users.
### Transparency: The program clearly displays computations and final totals, avoiding misleading calculations.

# Reference:

Association for Computing Machinery. (2018). ACM Code of Ethics and Professional Conduct. 
https://www.acm.org/code-of-ethics

# Contributors

#### Andrea Chloe G. Dando
#### Fritz Varun H. Tomines
#### Lit'le Tarcisse Janica D. Ensomo
