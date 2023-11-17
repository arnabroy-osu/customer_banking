# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    savings_acc_initial_balance = float(input("Enter your initial savings account balance (in USD): "))
    savings_acc_interest_rate = float(input("Enter your savings account interest rate (in %): "))
    savings_acc_months = int(input("Enter the number of months: "))
    
    # Call the create_savings_account function and pass the variables from the user.
    new_savings_balance, new_savings_interest = create_savings_account(savings_acc_initial_balance,savings_acc_interest_rate, savings_acc_months)
    
    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print("-------------------------------------------------------------------------------------------------------------------")
    print(f"Your updated savings account balance is $",'{:,.2f}'.format(new_savings_balance),"with $",'{:,.2f}'.format (new_savings_interest), "as total interest earned over a period of", '{:,.0f}'.format(savings_acc_months), "months")
    print("-------------------------------------------------------------------------------------------------------------------\n")

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_acc_deposit = float(input("Enter your CD account deposit (in USD): "))
    cd_acc_interest = float(input("Enter CD account interest rate (in %): "))
    cd_acc_maturity_in_months = int(input("Enter the number of months: "))
    
    # Call the create_cd_account function and pass the variables from the user.
    new_cd_balance, new_cd_interest = create_cd_account(cd_acc_deposit, cd_acc_interest, cd_acc_maturity_in_months)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("-------------------------------------------------------------------------------------------------------------------")
    print(f"Your CD account maturity amount is $",'{:,.2f}'.format(new_cd_balance),"with $",'{:,.2f}'.format(new_cd_interest), "as total interest earned over a period of", '{:,.0f}'.format(cd_acc_maturity_in_months), "months")
    print("-------------------------------------------------------------------------------------------------------------------\n")

if __name__ == "__main__":
    # Call the main function.
    main()
