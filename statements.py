#input data
current_bal: int = 500
min_withdrawal: int = 20
max_withdrawal: int = 1000

#Exit function
def exit():
    print ("Thank you for choosing our bank! Have a good day!")
def failure():
    print ("Transaction failed. Try again")


#Transaction function
def transaction(current_bal):
    while True:
        cashamount:int = int(input("Enter cash amount to be withdrawn: "))
        if cashamount <= current_bal and cashamount <= max_withdrawal and cashamount >= min_withdrawal:
            current_bal -= cashamount
            print("Transaction successful. Remaining balance:", current_bal)              
        elif cashamount > max_withdrawal or cashamount < min_withdrawal:
            print("This transaction cannot be processed. Withdrawal limits are violated. Your current balance is: ", current_bal)            
        elif cashamount > current_bal:
            print("Transaction failed. Insufficient funds. Your current balance is: ", current_bal)            
        else:
            break
        proceed = input("Do you want to proceed? y/n: ")
        if proceed == "y":            
            continue   
        elif proceed == "n":
            exit()
            break 
        else:
            failure()     
            break
    return current_bal      


#Main code
user_input=input("Do you want to withdraw cash? Enter y or n: ")
if user_input=="y":
    result = transaction(current_bal)
elif user_input=="n":
    exit()
else:
    failure()
    