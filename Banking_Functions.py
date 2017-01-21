import sqlite3
import time
import random

first_name= ['Warren','Claire','Sonia','Jane','Benjamin','Simon','Frank','Brandon','Julian','Jacob','Jason',
            'Blake','Adrian','Caroline','Katherine','Leonard','Eric','Madeleine','Andrea','Michelle','Anne',
            'Lauren','Diana','Lucas','Victor','Luke','Gavin','Julia','Sean','Phil','Edward','Virginia','Matt',
            'Angela','James','Sam','Victoria','Felicity','Mary','Adam','Peter','Austin','Ruth','Kimberly','Brian',
            'Lily','Yvonne','Joe','John','Jonathan','Wendy','Ella','Megan','Robert','Colin','Kevin','Pippa','Carol',
            'Natalie','Jessica','Michael','Emily','Christopher','Andrew','Max','Bernadette','Joan','Dominic','Leah',
            'Karen','Amelia']

last_name = ['Abraham','Mackay','Smith','Terry','Churchill','Walsh','Springer','Bell','Forsyth','Edmunds','Grant',
            'Lawrence','Wright','Pullman','Rutherford','Hill','Greene','Bower','McGrath','Taylor','Stewart','White',
            'Rees','Hamilton','Gibson','Mills','Glover','Metcalfe','Peters','Nash','Lee','Quinn','Hunter','Chapman',
            'North','Paige','Ferguson','Black','Scott','Hodges','Payne','Ogden','Hart','MacLeod','Hughes','Wilkins',
            'Short','Russell','Jackson','Newman','Paterson','Davies','Brown','Mathis','Anderson','Murray','Clark',
            'Jones','May','Duncan','Kerr','Watson','Buckland','Davidson','Kelly','Poole','MacDonald','Sharp',
            'Rampling','Powell','Butler']


non_used_list = ['ABC100000','ABC100001','ABC100002','ABC100003','ABC100004','ABC100005','ABC100006','ABC100007',
                 'ABC100008','ABC100009','ABC100010','ABC100011','ABC100012','ABC100013','ABC100014','ABC100015',
                 'ABC100016','ABC100017','ABC100018','ABC100019','ABC100020','ABC100021','ABC100022','ABC100023',
                 'ABC100024','ABC100025','ABC100026','ABC100027','ABC100028','ABC100029','ABC100030','ABC100031',
                 'ABC100032','ABC100033','ABC100034','ABC100035','ABC100036','ABC100037','ABC100038','ABC100039',
                 'ABC100040','ABC100041','ABC100042','ABC100043','ABC100044','ABC100045','ABC100046','ABC100047',
                 'ABC100048','ABC100049','ABC100050','ABC100051','ABC100052','ABC100053','ABC100054','ABC100055',
                 'ABC100056','ABC100057','ABC100058','ABC100059','ABC100060','ABC100061','ABC100062','ABC100063',
                 'ABC100064','ABC100065','ABC100066','ABC100067','ABC100068','ABC100069','ABC100070','ABC100071',
                 'ABC100072','ABC100073','ABC100074','ABC100075','ABC100076','ABC100077','ABC100078','ABC100079',
                 'ABC100080','ABC100081','ABC100082','ABC100083','ABC100084']


S_non_used_list = ['SAV100000', 'SAV100001', 'SAV100002', 'SAV100003', 'SAV100004', 'SAV100005', 'SAV100006',
                   'SAV100007', 'SAV100008', 'SAV100009', 'SAV100010', 'SAV100011', 'SAV100012', 'SAV100013',
                   'SAV100014', 'SAV100015', 'SAV100016', 'SAV100017', 'SAV100018', 'SAV100019', 'SAV100020',
                   'SAV100021', 'SAV100022', 'SAV100023', 'SAV100024', 'SAV100025', 'SAV100026', 'SAV100027',
                   'SAV100028', 'SAV100029', 'SAV100030', 'SAV100031', 'SAV100032', 'SAV100033', 'SAV100034',
                   'SAV100035', 'SAV100036', 'SAV100037', 'SAV100038', 'SAV100039', 'SAV100040', 'SAV100041',
                   'SAV100042', 'SAV100043', 'SAV100044', 'SAV100045', 'SAV100046', 'SAV100047', 'SAV100048',
                   'SAV100049', 'SAV100050', 'SAV100051', 'SAV100052', 'SAV100053', 'SAV100054', 'SAV100055',
                   'SAV100056', 'SAV100057', 'SAV100058', 'SAV100059', 'SAV100060', 'SAV100061', 'SAV100062',
                   'SAV100063', 'SAV100064', 'SAV100065', 'SAV100066', 'SAV100067', 'SAV100068', 'SAV100069',
                   'SAV100070', 'SAV100071', 'SAV100072', 'SAV100073', 'SAV100074', 'SAV100075', 'SAV100076',
                   'SAV100077', 'SAV100078', 'SAV100079', 'SAV100080', 'SAV100081', 'SAV100082', 'SAV100083',
                   'SAV100084']

#keep adding more unique IDs to this list and run insert_unassigned_ids to dump them to SQl table

conn = sqlite3.connect("XYZ Python Code.db")
c = conn.cursor()

# Checking Acct TABLES
# ASSIGNED_IDS ::> Assigned_Ids
# CustomerInformation  ::> Account_ID :: Name :: Account_Open_Date
# CustomerTransactions ::> Account_ID :: Trans_Amt :: Trans_Date
# UNASSIGNED_IDS  ::> Un_Assigned_Ids

# Savings Acct TABLES
# Savings_Assigned_Ids ::> S_Assigned_Ids
# Savings_CustomerInformation  ::> S_Account_ID :: S_Name :: S_Account_Open_Date
# Savings_CustomerTransactions ::> S_Account_ID :: S_Trans_Amt :: S_Trans_Date
# Savings_UNASSIGNED_IDS  ::> S_Un_Assigned_Ids


def insert_unassigned_ids(account_type):
    if account_type == "Checking Account":
        for every_id in non_used_list:
            print every_id
            c.execute("INSERT INTO UNASSIGNED_IDS (Un_Assigned_Ids) VALUES (?)",(every_id,))
            conn.commit()

    elif account_type == "Savings Account":
        for every_id in S_non_used_list:
            print every_id
            c.execute("INSERT INTO Savings_UNASSIGNED_IDS (S_Un_Assigned_Ids) VALUES (?)",(every_id,))
            conn.commit()
#insert unassigned ids to the unassigned table


def possible_account_ids(account_type):
    if account_type == "Checking Account":
        c.execute("SELECT UN_Assigned_Ids FROM UNASSIGNED_IDS")
        customerIDs= c.fetchall()
        return customerIDs

    if account_type == "Savings Account":
        c.execute("SELECT S_UN_Assigned_Ids FROM Savings_UNASSIGNED_IDS")
        customerIDs= c.fetchall()
        return customerIDs
# returns all un-assigned ids from UNASSIGNED_IDS table


def assigned_account_ids(account_type):
    if account_type == "Checking Account":
        c.execute("SELECT Assigned_Ids FROM ASSIGNED_IDS")
        assigned_customerIDs= c.fetchall()

    elif account_type == "Savings Account":
        c.execute("SELECT S_Assigned_Ids FROM Savings_Assigned_Ids")
        assigned_customerIDs= c.fetchall()

    return assigned_customerIDs
#returns all assigned ids from ASSIGNED_IDS table


def swap_and_delete(account_type,customer_id):
    if account_type == "Checking Account":
        c.execute("INSERT INTO ASSIGNED_IDS (Assigned_Ids) VALUES (?)",(customer_id,))
        c.execute("delete from UNASSIGNED_IDS where Un_Assigned_Ids = '%s' " % customer_id)
        conn.commit()

    elif account_type == "Savings Account":
        c.execute("INSERT INTO Savings_ASSIGNED_IDS (S_Assigned_Ids) VALUES (?)",(customer_id,))
        c.execute("delete from Savings_UNASSIGNED_IDS where S_Un_Assigned_Ids = '%s' " % customer_id)
        conn.commit()
# swap and delete in assigned & unassigned tables


def gather_customer_info(account_type,customer_id):
   active_account_ID = customer_id
   name = random.choice(first_name) + " " + random.choice(last_name)
   account_open_date = time.strftime("%Y-%m-%d %H:%M")
   c.execute("INSERT INTO CustomerInformation (Account_ID, Name, Account_Open_Date) VALUES (?, ?, ?)",
          (active_account_ID,name,account_open_date))
   conn.commit()
# get new random customer and add ID, name & account open date to table


def Transactions_Deposit(account_type,customer_id):
    Trans_Amt_Dep = float(random.randrange(1000,50000))
    Trans_Date_Dep = time.strftime("%Y-%m-%d %H:%M")
    Transaction_Type = "Deposit"

    if account_type == "Checking Account":
        c.execute("INSERT INTO CustomerTransactions(Account_ID,Trans_Amt,Trans_Date,Transaction_Type) VALUES (?,?,?,?)",
                  (customer_id,Trans_Amt_Dep,Trans_Date_Dep,Transaction_Type))
        conn.commit()

    elif account_type == "Savings Account":
        c.execute("INSERT INTO Savings_CustomerTransactions(S_Account_ID,S_Trans_Amt,S_Trans_Date,S_Transaction_Type) "
                  "VALUES (?,?,?,?)",
                  (customer_id,Trans_Amt_Dep,Trans_Date_Dep,Transaction_Type))
        conn.commit()
#Deposit Cash


def Transactions_Withdrawal(account_type,customer_id,amount):

    Trans_Date_With = time.strftime("%Y-%m-%d %H:%M")
    Transaction_Type = "Withdrawal"

    if account_type == "Checking Account":
        c.execute("INSERT INTO CustomerTransactions(Account_ID,Trans_Amt,Trans_Date,Transaction_Type) VALUES (?,?,?,?)",
                  (customer_id,amount,Trans_Date_With,Transaction_Type))
        conn.commit()

    elif account_type == "Savings Account":
        c.execute("INSERT INTO Savings_CustomerTransactions(S_Account_ID,S_Trans_Amt,S_Trans_Date,S_Transaction_Type) "
                  "VALUES (?,?,?,?)",
                  (customer_id,amount,Trans_Date_With,Transaction_Type))
        conn.commit()
#Withdraw Cash


def Sum_Total_Balance(account_type,customer_id):
    if account_type == "Checking Account":
        c.execute("SELECT SUM(Trans_Amt) FROM CustomerTransactions WHERE Account_ID =(?)",(customer_id,))
        sum_total = c.fetchall()[0][0]
        return sum_total
    elif account_type == "Savings Account":
        c.execute("SELECT SUM(Trans_Amt) FROM Savings_CustomerTransactions WHERE S_Account_ID =(?)",(customer_id,))
        sum_total = c.fetchall()[0][0]
        return sum_total
#Check Account Balance


def Transaction_Wire(customer_id_sender,customer_id_receiver):
    wire_sender = customer_id_sender
    wire_receiver = customer_id_receiver
    wire_amt = random.randint(100,500)
    wire_date = time.strftime("%Y-%m-%d %H:%M")
    wire_code = "Wire Transfer"

    if wire_amt > Sum_Total_Balance("Checking Account", wire_sender):
        pass

    else:

        #Decrease Sender's bank balance
        c.execute("INSERT INTO CustomerTransactions(Account_ID,Trans_Amt,Trans_Date,Transaction_Type) VALUES (?,?,?,?)",
              (wire_sender,-(wire_amt),wire_date,wire_code + " To " + wire_receiver))

        #Increase Receiver's bank balance
        c.execute("INSERT INTO CustomerTransactions(Account_ID,Trans_Amt,Trans_Date,Transaction_Type) VALUES (?,?,?,?)",
              (wire_receiver,wire_amt,wire_date,wire_code + " From " + wire_sender))
        conn.commit()
#Make a wire transfer from checking to checking accounts


def Online_Bill_Pay(customer_id):
    bill_payer = customer_id
    bill_amt = random.randint(50,100)
    bill_pay_date = time.strftime("%Y-%m-%d %H:%M")
    bill_type1 = random.choice(["Electricity","Internet","Phone","Magazine Subscription","Water","Gardening Service"])
    bill_type2 = "Bill payment for " + bill_type1

    if bill_amt > Sum_Total_Balance("Checking Account",bill_payer):
        pass
    else:
        #Pay the bill
        c.execute("INSERT INTO CustomerTransactions(Account_ID,Trans_Amt,Trans_Date,Transaction_Type) VALUES (?,?,?,?)",
              (bill_payer,-(bill_amt),bill_pay_date,bill_type2))
#Make a bill payment for various utility charges


def Account_Fee():
    last_date_for_fee = "2016/12/30"
    today_date = time.strftime("%Y-%m-%d")

    if today_date > last_date_for_fee is True:
        return True
    else:
        return False
#Charge Annual Account Maintenance fee


def Account_Fee_Charge(customer_id,amount):
    Fee_Date = time.strftime("%Y-%m-%d %H:%M")
    Transaction_Type = "Account Maintenance Fee"
    c.execute("INSERT INTO CustomerTransactions(Account_ID,Trans_Amt,Trans_Date,Transaction_Type) VALUES (?,?,?,?)",
              (customer_id,amount,Fee_Date,Transaction_Type))
    conn.commit()
#Insert Account Fee charge to DB


def Print_Account_Statement(account_type,customer_id):

    if account_type == "Checking Account":

        c.execute("SELECT Trans_Amt,Trans_Date, Transaction_Type FROM CustomerTransactions WHERE Account_ID =(?)",
                  (customer_id,))
        all_transactions = c.fetchall()
        c.execute("SELECT Name FROM CustomerInformation WHERE Account_ID = (?)",(customer_id,))
        customer_name = c.fetchone()[0]
        today_date = time.strftime("%Y-%m-%d")

        bank_statement = "/Users/kungalama/PycharmProjects/BankingProject/Bank_Statement.txt"
        f = open(bank_statement, "a")

        f.write('{} {} {} {:>10}'.format("Checking Account ","Customer Statement",customer_name,today_date)+ "\n")
        f.write("")

        transaction_sequence = 0

        for transaction_X in all_transactions:
            transaction_sequence += 1
            AmountX = transaction_X[0]
            t_date = transaction_X[1]
            t_type = transaction_X[2]
            f.write('{:>3}   ${:>10,.2f} {} {}'.format(transaction_sequence,AmountX,t_date,t_type)+ "\n")

        sum_total_balance = Sum_Total_Balance("Checking Account",customer_id)
        f.write('{:>16}'.format("_________")+"\n")
        f.write('{}{:>16,.2f} {}'.format("$",sum_total_balance, " :Total Balance"))

        f.close()

    elif account_type == "Savings Account":
        c.execute("SELECT S_Trans_Amt,S_Trans_Date, S_Transaction_Type FROM Savings_CustomerTransactions WHERE"
                  " S_Account_ID =(?)",
                  (customer_id,))
        all_transactions = c.fetchall()
        c.execute("SELECT S_Name FROM Savings_CustomerInformation WHERE S_Account_ID = (?)",(customer_id,))
        customer_name = c.fetchone()[0]
        today_date = time.strftime("%Y-%m-%d")

        bank_statement = "/Users/kungalama/PycharmProjects/BankingProject/Bank_Statement.txt"
        f = open(bank_statement, "a")

        f.write('{} {} {} {:>10}'.format("Savings Account ","Customer Statement",customer_name,today_date)+ "\n")
        f.write("")

        transaction_sequence = 0

        for transaction_X in all_transactions:
            transaction_sequence += 1
            AmountX = transaction_X[0]
            t_date = transaction_X[1]
            t_type = transaction_X[2]
            f.write('{:>3}   ${:>10,.2f} {} {}'.format(transaction_sequence,AmountX,t_date,t_type)+ "\n")

        sum_total_balance = Sum_Total_Balance("Savings Account",customer_id)
        f.write('{:>16}'.format("_________")+"\n")
        f.write('{}{:>16,.2f} {}'.format("$",sum_total_balance, " :Total Balance"))

        f.close()
#Prints Account Statement for customers


def Customer_Name(account_type,customer_id):
    if account_type == "Checking Account":
        c.execute("SELECT Name FROM CustomerInformation WHERE Account_ID =(?)",(customer_id,))
        Name = c.fetchall()[0][0]
        return Name
    elif account_type == "Savings Account":
        c.execute("SELECT Name FROM Savings_CustomerInformation WHERE S_Account_ID =(?)",(customer_id,))
        Name = c.fetchall()[0][0]
        return Name
#Get Customer name


def Sav_interest_rate(account_type,customer_id):
    if account_type == "Savings Account":
        balance_without_interest = Sum_Total_Balance(account_type,customer_id)
        interest_rate_percent = 0.05
        balance_with_interest = balance_without_interest * (1+interest_rate_percent)
        return balance_with_interest

    else:
        return None



