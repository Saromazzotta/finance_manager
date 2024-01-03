import csv
import gspread
import time
from pprint import pprint
from expenses import (SALARY,
                        SUBSCRIPTION_NAMES, 
                        CREDIT_CARD_NAMES, 
                        MEDICAL_BILLS, 
                        HYGIENE, 
                        MONEY_TRANSFERS_OUT, 
                        GROCERIES,
                        GIFTS,
                        PERSON, 
                        EATING_OUT, 
                        ENTERTAINMENT,
                        EDUCATION,
                        TRANSPORT_AND_TRAVEL
    )



MONTH = "december"

file = f"sofi_{MONTH}.csv"

transactions = []

def sofi_bank(file,
                SALARY, 
                SUBSCRIPTION_NAMES, 
                CREDIT_CARD_NAMES, 
                MEDICAL_BILLS, 
                HYGIENE, 
                MONEY_TRANSFERS, 
                GROCERIES,
                GIFTS,
                EATING_OUT, 
                PERSON, 
                ENTERTAINMENT,
                EDUCATION,
                TRANSPORT_AND_TRAVEL):

    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Skip the header row
        header = next(csv_reader)
        
        for row in csv_reader:
            date = row[0]
            name = row[1] 

            if row[3] == 'Amount':
                continue

            try:
                amount = float(row[3])
                print("Converted Float:", amount)
            except ValueError:
                print("Invalid string format for conversion to float")

            print("Name from CSV:", repr(name))
                
            if name in CREDIT_CARD_NAMES:
                category = "Credit Card Payments"
            elif name in SUBSCRIPTION_NAMES:
                category = "Subscriptions"
            elif name in MONEY_TRANSFERS:
                category = "Money Transfers Out" 
            elif name in ENTERTAINMENT:
                category = "Entertainment"
            elif name in EDUCATION: 
                category = "Education"
            elif name in HYGIENE:
                category= "Hygiene"
            elif name in MEDICAL_BILLS:
                category = "Medical"
            elif name in TRANSPORT_AND_TRAVEL:
                category = "Transport & Travel"
            elif amount > 0 and name != "JLD FITNESS LLC":
                category = "Other Income"
            elif name in SALARY:
                category = "Salary"
            elif name in GROCERIES:
                category = "Groceries"
            elif name in GIFTS:
                category = "Gifts"
            elif name in EATING_OUT:
                category = "Eating Out"
            else:
                category = "Other"
                print("Unknown case - Name:", repr(name), "Amount:", amount)

            pprint(name)


            transaction = ((date, name, category, amount))
            transactions.append(transaction)
        return transactions
    


# Authenticated gspread client
sa = gspread.service_account()

# Open the Google Sheets file
sh = sa.open("Personal Finances")

# Get the worksheet by name
wks = sh.worksheet(f"{MONTH}")

# Get categorized transactions
rows = sofi_bank(file, 
                    SALARY,
                    SUBSCRIPTION_NAMES, 
                    CREDIT_CARD_NAMES, 
                    MEDICAL_BILLS, 
                    HYGIENE, 
                    MONEY_TRANSFERS_OUT, 
                    GROCERIES,
                    GIFTS,
                    PERSON, 
                    EATING_OUT, 
                    ENTERTAINMENT,
                    EDUCATION,
                    TRANSPORT_AND_TRAVEL
)

pprint(rows)


for row in rows:
    wks.insert_row([row[0], row[1], row[2], row[3]] ,8)
    time.sleep(2)