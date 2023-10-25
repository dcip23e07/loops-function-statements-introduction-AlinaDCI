#input data
current_bal = 500
min_withdrawal = 20
max_withdrawal = 1000

#Exit function
def exit():
    print ("Thank you for choosing our bank! Have a good day!")

#Transaction function
def transaction(current_bal):
    while True:
        cashamount:int = int(input("Enter cash amount to be withdrawn: "))
        if cashamount <= current_bal and cashamount <= max_withdrawal and cashamount >= min_withdrawal:
            current_bal -= cashamount
            print("Transaction successful. Remaining balance:", current_bal )
            break
        elif cashamount > max_withdrawal or cashamount < min_withdrawal:
            print("This transaction cannot be processed. Withdrawal limits are violated")
            break
        elif cashamount > current_bal:
            print("Transaction failed. Insufficient funds")
            break
        else:
            break
    return current_bal

#Main code
user_input=input("Do you want to withdraw cash? Enter y or n: ")
if user_input=="y":
    result = transaction(current_bal)
else:
    exit()

