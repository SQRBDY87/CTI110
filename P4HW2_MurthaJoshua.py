#CTI-110
#P4HW2-Expenses
#Joshua Murtha
#6/30/2022


account_balance = 0
ending_balance = 0
expense = 0
keep_going = "y"

account_balance = float(input("Enter starting amount in account: $"))

ending_balance = account_balance

for a in range (1000):
    while keep_going == "y":

       
        purchase = int(input("Enter expense: "))

        ending_balance = ending_balance - purchase

        expense = expense + 1

        keep_going = input("Do you want to enter another expense? (y/n)")

if keep_going == "n":
    print("Amount in account before expenses subtraction $", format (account_balance, ",.2f"))
    print("Number of expense entered:", expense)
    print("Amount in account AFTER expenses subtracted is $", format (ending_balance, ",.2f"))
