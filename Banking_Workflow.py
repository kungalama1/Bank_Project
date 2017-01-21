from Banking_Functions import insert_unassigned_ids
from Banking_Functions import possible_account_ids
from Banking_Functions import swap_and_delete
from Banking_Functions import gather_customer_info
from Banking_Functions import assigned_account_ids
from Banking_Functions import Transactions_Deposit
from Banking_Functions import Transactions_Withdrawal
from Banking_Functions import Sum_Total_Balance
from Banking_Functions import Transaction_Wire
from Banking_Functions import Online_Bill_Pay
from Banking_Functions import Account_Fee
from Banking_Functions import Account_Fee_Charge
from Banking_Functions import Print_Account_Statement

import random
import datetime

todayDate = datetime
bank_statement = "/Users/kungalama/PycharmProjects/BankingProject/Bank_Statement.txt"
account_list = ["Checking Account", "Savings Account"]


#insert unassigned ids when new ids are added to non_used_list in Banking_Functions module
#with the For loop with the random customerX put customer info into info table & Swap the CustomerX
#from the unassigned to the assigned table and put info for the CustomerX in the Info table.
#insert_unassigned_ids()
# for every_random_customer in range(1,random.randrange(len(possible_account_ids()))):
#     customerX= random.choice(possible_account_ids())
#
#     gather_customer_info(cubstomerX[0])
#     swap_and_delete(customerX[0])

account_type = random.choice(account_list)

if account_type == "Checking Account":

    for every_random_customer in range(1,random.randrange(len(assigned_account_ids(account_type)))):
        activity_case = random.randint(1,4)

        if activity_case == 1:

            customerX_Deposit= random.choice(assigned_account_ids(account_type))
            Transactions_Deposit("Checking Account",customerX_Deposit[0])

        elif activity_case == 2:

            CustomerX_Withdrawal = random.choice(assigned_account_ids(account_type))
            balance = Sum_Total_Balance(account_type,CustomerX_Withdrawal[0])
            with_random_amt = random.randrange(-1000,-10000,-100)

            if balance < with_random_amt:
                pass
            else:
                Transactions_Withdrawal("Checking Account", CustomerX_Withdrawal[0],with_random_amt)

        elif activity_case ==3:
            CustomerX_Wiring = random.sample(assigned_account_ids(account_type),2)
            wire_sender = CustomerX_Wiring[0][0]
            wire_receiver = CustomerX_Wiring[1][0]

            Transaction_Wire(wire_sender,wire_receiver)

        elif activity_case ==4:
            CustomerX_Bill_Pay = random.sample(assigned_account_ids(account_type),2)
            bill_payer = CustomerX_Bill_Pay[0][0]
            Online_Bill_Pay(bill_payer)

elif account_type == "Savings Account":

    customerX_Deposit= random.choice(assigned_account_ids(account_type))
    Transactions_Deposit("Savings Account",customerX_Deposit[0])

Print_Account_Statement("Checking Account","ABC100013")
#Print Account Statement for a customer



""" Charge Account Maintenance fee if date parameter is met.
## Activate near year end ###
# Annual_fee_status = Account_Fee()
#
# if Annual_fee_status is True:
#     for every_customer in assigned_account_ids():
#         Account_Fee_Charge(every_customer,5.00)
# else:
#     pass

"""


