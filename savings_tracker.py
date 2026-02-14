print("Savings Tracker")
print("Enter your monthly savings below:")

tts = 0  # Initialize total savings

for month in range(1,13):  # LOOP: Collects monthly savings using a for loop (12 times for 12 months)
    s = float(input("Month " + str(month) + " savings: ")) # Ask user to input savings for each month
    tts = tts + s # Adds savings to the current total savings

print("Total savings before any bonuses and emergency withdrawals: $",tts)

b = str(input("Did you receive a bonus this year? Yes or No:")) # Asks if the user received a bonus or not

if b =="Yes":
    b = float(input("Enter total amount amount of the bonus: "))  # Asks for bonus amount to add it to total savings
    tts = tts + b # Adds the entered amount of bonus to the current total savings
    print("Bonus added!")
    print("Current savings after bonus: $",tts)
elif b == "No":
    print("No bonus received.")
else:  # Handles invalid bonus input
    print("Invalid input.Assuming no bonus received.")

e = input("Do you want to withdraw for emergencies? Yes or No:") # Asks if the user wants to withdraw money for emergencies
if e =="Yes": 
    w = float(input("Enter the withdrawal amount: $"))   # Asks how much they want to withdraw
    if w > tts:
        print("WARNING : Withdrawal amount exceeds savings.Setting final savings to $0")   # To prevent negative savings
        tts = 0
    elif tts > w:
        tts = tts - w # Deducts withdrawal amount from total savings
        print("Withdrawal successful.")
    else:
        print("Invalid input. Assuming no withdrawal") # Handles non-numeric input
elif e == "No":
     print("No withdrawal made.")
else:
     print("Invalid input. Assuming no withdrawal")  # Handles unexpected input

print("Final savings after adjustments: $", tts)
print("Thank you for using the Savings tracker!")
