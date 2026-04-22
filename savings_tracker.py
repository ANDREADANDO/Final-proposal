import json
import tkinter as tk
from tkinter import messagebox, scrolledtext
import os

# Get the directory where the script is located to ensure the file is easy to find
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
FILE_PATH = os.path.join(SCRIPT_DIR, "savings_record.json")

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

# ---------------- SAVINGS FUNCTIONS ----------------
def analyze_savings(savings):
    total = sum(savings)
    average = total / len(savings) if len(savings) > 0 else 0
    highest = max(savings)
    lowest = min(savings)
    highest_month = months[savings.index(highest)]
    lowest_month = months[savings.index(lowest)]
    analysis = (
        f"Total Savings (before adjustments): ${total}\n"
        f"Average Monthly Savings: ${average:.2f}\n"
        f"Highest Saving Month: {highest_month} (${highest})\n"
        f"Lowest Saving Month: {lowest_month} (${lowest})"
    )
    return total, analysis

def evaluate_goal(final_total, goal):
    if final_total >= goal:
        return "🎉 Congratulations! You achieved your savings goal."
    else:
        difference = goal - final_total
        percentage = (final_total / goal * 100) if goal > 0 else 0
        return (
            "You did not reach your savings goal.\n"
            f"You are ${difference:.2f} short.\n"
            f"You achieved {percentage:.2f}% of your goal."
        )

def save_to_file(data):
    try:
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, "r") as file:
                existing_data = json.load(file)
            if isinstance(existing_data, dict):
                existing_data = [existing_data]
        else:
            existing_data = []
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []

    existing_data.append(data)
    with open(FILE_PATH, "w") as file:
        json.dump(existing_data, file, indent=4)

# ---------------- VIEW HISTORY FUNCTION ----------------
def show_history():
    history_window = tk.Toplevel(root)
    history_window.title("Saved History")
    history_window.geometry("400x400")

    text_area = scrolledtext.ScrolledText(history_window, width=45, height=20)
    text_area.pack(padx=10, pady=10)

    try:
        with open(FILE_PATH, "r") as file:
            data = json.load(file)
            if not data:
                text_area.insert(tk.END, "No records found.")
            else:
                for i, record in enumerate(data, 1):
                    text_area.insert(tk.END, f"--- Record #{i} ---\n")
                    text_area.insert(tk.END, f"Goal: ${record['goal']}\n")
                    text_area.insert(tk.END, f"Final Total: ${record['final_total']}\n")
                    text_area.insert(tk.END, "-"*20 + "\n")
    except FileNotFoundError:
        text_area.insert(tk.END, "No storage file found yet. Save some data first!")
    
    text_area.configure(state='disabled') # Prevent user from editing history window

# ---------------- GUI FUNCTION ----------------
def run_tracker():
    try:
        goal = float(goal_entry.get() or 0)
        bonus = float(bonus_entry.get() or 0)
        withdrawal = float(withdraw_entry.get() or 0)
        
        savings = []
        for entry in month_entries:
            val = float(entry.get() or 0)
            savings.append(val)

        # VALIDATION: Stop everything if a negative is found before math begins
        all_inputs = [goal, bonus, withdrawal] + savings
        if any(n < 0 for n in all_inputs):
            messagebox.showerror("Invalid Input", "Negative values are not allowed. Please try again.")
            return 

        total, analysis = analyze_savings(savings)
        total += bonus
        total -= withdrawal
        
        result_text = f"{analysis}\n\nFinal Savings After Adjustments: ${total}\n\n"
        result_text += evaluate_goal(total, goal)
        result_label.config(text=result_text)
        
        save_data = {
            "goal": goal,
            "monthly_savings": savings,
            "bonus": bonus,
            "withdrawal": withdrawal,
            "final_total": total
        }
        save_to_file(save_data)
        messagebox.showinfo("Saved", f"Saved to:\n{FILE_PATH}")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Savings Tracker")
root.geometry("450x850")

tk.Label(root, text="Savings Tracker", font=("Arial", 16, "bold")).pack(pady=10)

# Goal
tk.Label(root, text="Yearly Savings Goal").pack()
goal_entry = tk.Entry(root)
goal_entry.pack()

# Monthly savings
tk.Label(root, text="Monthly Savings").pack(pady=10)
month_entries = []
for i in range(12):
    frame = tk.Frame(root)
    frame.pack(fill="x", padx=50)
    tk.Label(frame, text=months[i], width=10, anchor="w").pack(side="left")
    entry = tk.Entry(frame, width=15)
    entry.pack(side="right", padx=5)
    month_entries.append(entry)

# Bonus & Withdrawal
tk.Label(root, text="Bonus Amount").pack(pady=5)
bonus_entry = tk.Entry(root)
bonus_entry.pack()

tk.Label(root, text="Total Withdrawal").pack(pady=5)
withdraw_entry = tk.Entry(root)
withdraw_entry.pack()

# Buttons
btn_frame = tk.Frame(root)
btn_frame.pack(pady=20)

tk.Button(btn_frame, text="Run & Save", command=run_tracker, bg="lightgreen", width=15).pack(side="left", padx=5)
tk.Button(btn_frame, text="View History", command=show_history, bg="lightblue", width=15).pack(side="left", padx=5)

# Results
result_label = tk.Label(root, text="", wraplength=380, justify="left", font=("Arial", 10))
result_label.pack(pady=10)

root.mainloop()
