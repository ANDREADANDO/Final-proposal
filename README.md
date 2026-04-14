# Savings Tracker

## Project Overview
The Savings Tracker is a Python-based financial tracking application with a graphical user interface (GUI) built using Tkinter. It allows users to input monthly savings, bonuses, and withdrawals, then calculates total savings, analyzes financial performance, and evaluates whether a yearly savings goal has been achieved.

The project demonstrates key programming concepts such as loops, functions, file handling, GUI development, conditional logic, and data persistence using JSON.

## Updated Feature List
- Collects 12 months of savings input through a GUI  
- Calculates total annual savings  
- Computes average, highest, and lowest monthly savings  
- Identifies highest and lowest saving months  
- Allows input of bonus income and withdrawals  
- Computes final adjusted savings  
- Compares results against a user-defined savings goal  
- Provides performance feedback (goal achieved or not)  
- Saves all records to a JSON file (`savings_record.json`)  
- Handles invalid inputs using error checking and exceptions  

## Technologies Used
- **Python 3.13+** – Core programming language used for logic and computation  
- **Tkinter** – Built-in Python library used to create the graphical user interface  
- **JSON** – Used for saving and storing user financial records persistently  

Python was chosen for its simplicity, readability, and strong support for GUI development and data handling.

## Detailed Methodology

### 1. Monthly Savings Input
The GUI provides 12 input fields representing each month of the year. Users enter their savings per month, which are stored in a list and processed using iteration.

### 2. Savings Analysis
The program calculates:
- Total savings  
- Average monthly savings  
- Highest and lowest savings  
- Corresponding months for highest and lowest values  

### 3. Adjustments (Bonus and Withdrawal)
After initial computation:
- Bonus amounts are added to total savings  
- Withdrawal amounts are deducted from total savings  

### 4. Goal Evaluation
The final adjusted total is compared to the user’s savings goal:
- If the goal is met or exceeded, a success message is displayed.
- Otherwise, the program shows the shortfall and percentage achieved. 

### 5. Data Storage
All savings records are stored in `savings_record.json`, allowing users to track past entries and results.

## File Structure( in no particular order)
#### --> savings_tracker.py
#### --> README.md
#### --> CHANGELOG.md

The structure is intentionally minimal to maintain clarity and organization.

# Installation and Execution Instructions

1. Install Python 3.13.7 or newer.
2. Clone this repository or download the source file.9
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

##### Respect for Intellectual Property: All code in this repository was written by the contributors. No external code was copied without attribution.
##### User Privacy: The program does not collect, store, or transmit user financial data. All input remains temporary during execution.
##### Accessibility: The interface uses clear prompts and straightforward instructions to ensure usability for beginner users.
##### Transparency: The program clearly displays computations and final totals, avoiding misleading calculations.

# Reference:

Association for Computing Machinery. (2018). ACM Code of Ethics and Professional Conduct. 
https://www.acm.org/code-of-ethics

# Contributors

#### Andrea Chloe G. Dando
#### Fritz Varun H. Tomines
#### Lit'le Tarcisse Janica D. Ensomo
