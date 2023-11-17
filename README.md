# Customer Banking Application

## Overview: 
This customer banking application is written in python which will allow users to calculate and track interest earned on savings and CD accounts. By running this application, users will be able to enter their savings and CD account information, see the interest earned, and view the updated balance or maturity amount after a specified number of months.

## Pseudo Source Code
Our Source code consists of 4 python files or source code module, namely:
    1. Accounts.py
    2. savings_account.py
    3. cd_account.py
    4. customer_banking.py

Description of each python file:
    1. Accounts.py : 
        This file contains the account class and set the methods to set the balance and interest 

    2. savings_account.py : 
        In this file, we import the Account class (which is defined in Accounts.py) & defines a ‘create_savings_account’ function which will create a savings account instance. It calculates the total interest earned based on Initial balance, Interest Rate and duration in months which are provided by the user during runtime. And then it updates the account balance by adding the total interest with the initial balance. The function then finally returns the updated balance and total interest earned.

    3. cd_account.py
        This file is similar to the previous file (savings_account.py) in terms of the code structure and the functionality – but here it takes care of the ‘CD Account’ portion of the Customer Banking Application. It creates a ‘create_cd_account’ function that creates a CD account instance. It calculates the total interest earned based on Initial Deposit, Interest Rate and duration in months. And then it calculates maturity amount of the CD account by adding the interest with the initial deposit. And finally like the previous file, it also returns the maturity amount and total interest earned.


    4. customer_banking.py
    This is the python file which will be executed to implement the Customer Banking Application. Here we create a main function that prompts the user to enter the savings and CD account details (Initial Balance/deposit, Interest Rate & duration in months). Once the users input these values, the main function in turn calls the 2 functions - create_savings_account and create_cd_account functions (created in the python files - savings_account.py & cd_account.py that makes use of Account Class defined in Accounts.py) that calculates the total interest earned and updates the balances in savings account and calculates the final maturity amount in CD account & finally display the results.


## Assumption   
1. User would input the number of months in whole number for the app to work properly.

2. Total interest earned on Savings or CD accounts is calculated as below as per the instruction
    Interest = Balance * (Apr/100 * Months/12)
    
    where
    Interest = Total Interest earned
    Balance = Total Initial balanace on Saving account or CD account initial deposit
    Apr = Interest Rate 
    Months = Duration in months
