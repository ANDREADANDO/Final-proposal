import json
import tkinter as tk
from tkinter import messagebox

months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

# ---------------- SAVINGS FUNCTIONS ----------------
def analyze_savings(savings):
    total = sum(savings)
    average = total / len(savings)
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
        percentage = (final_total / goal) * 100
        return (
            "You did not reach your savings goal.\n"
            f"You are ${difference:.2f} short.\n"
            f"You achieved {percentage:.2f}% of your goal."
        )

def save_to_file(data):
    try:
        with open("savings_record.json", "r") as file:
            existing_data = json.load(file)
        if isinstance(existing_data, dict):
            existing_data = [existing_data]
    except (FileNotFoundError, json.JSONDecodeError):
        existing_data = []
    existing_data.append(data)
    with open("savings_record.json", "w") as file:
        json.dump(existing_data, file, indent=4)

# ---------------- GUI FUNCTION ----------------
def run_tracker():
    try:
        goal = float(goal_entry.get() or 0)
        savings = []
        for entry in month_entries:
            value = float(entry.get() or 0)
            savings.append(value)
        bonus = float(bonus_entry.get() or 0)
        withdrawal = float(withdraw_entry.get() or 0)
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
        messagebox.showinfo("Saved", "Savings data saved successfully!")
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers.")

# ---------------- GUI ----------------
root = tk.Tk()
root.title("Savings Tracker")
root.geometry("420x700")

tk.Label(root, text="Savings Tracker", font=("Arial", 16)).pack(pady=10)

# Goal
tk.Label(root, text="Yearly Savings Goal").pack()
goal_entry = tk.Entry(root)
goal_entry.pack()

# Monthly savings
tk.Label(root, text="Monthly Savings").pack(pady=10)
month_entries = []
for i in range(12):
    frame = tk.Frame(root)
    frame.pack()
    tk.Label(frame, text=months[i]).pack(side="left")
    entry = tk.Entry(frame, width=10)
    entry.pack(side="left", padx=5)
    month_entries.append(entry)

# Bonus
tk.Label(root, text="Bonus Amount").pack(pady=5)
bonus_entry = tk.Entry(root)
bonus_entry.pack()

# Withdrawal
tk.Label(root, text="Total Withdrawal").pack(pady=5)
withdraw_entry = tk.Entry(root)
withdraw_entry.pack()

# Run button
tk.Button(root, text="Run Savings Tracker", command=run_tracker).pack(pady=15)

# Results
result_label = tk.Label(root, text="", wraplength=380, justify="left")
result_label.pack(pady=10)

root.mainloop()
