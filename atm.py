# Initial account balance
account_balance = 50000  # UGX

# Ask the user how much they want to withdraw
withdrawal_amount = int(input("Enter amount to withdraw (UGX): "))

# Logic using if-else
if withdrawal_amount <= 0:
    print("Invalid amount. Please enter a positive number.")
elif withdrawal_amount > account_balance:
    print(f"Insufficient balance. You only have UGX {account_balance}.")
else:
    account_balance -= withdrawal_amount
    print(f"Withdrawal successful! You withdrew UGX {withdrawal_amount}.")
    print(f"Remaining balance: UGX {account_balance}")
