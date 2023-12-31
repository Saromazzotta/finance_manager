import csv
import gspread
import time
from pprint import pprint
from expenses import (SUBSCRIPTION_NAMES, 
                        CREDIT_CARD_NAMES, 
                        MEDICAL_NAMES, 
                        HYGIENE, 
                        MONEY_TRANSFERS_OUT, 
                        GROCERIES, 
                        PERSON, 
                        EATING_OUT, 
                        ENTERTAINMENT,
                        GAS_AND_TRANSPORTATION)



MONTH = "november"

file = f"sofi_{MONTH}.csv"

transactions = []

def sofi_bank(file, 
                SUBSCRIPTION_NAMES, 
                CREDIT_CARD_NAMES, 
                MEDICAL_NAMES, 
                HYGIENE, 
                MONEY_TRANSFERS, 
                GROCERIES, 
                EATING_OUT, 
                PERSON, 
                ENTERTAINMENT,
                GAS_AND_TRANSPORTATION):

    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)

        # Skip the header row
        header = next(csv_reader)
        
        for row in csv_reader:
            date = row[0]
            name = row[1] 

            if row[3] == 'amount':
                continue
            try:
                amount = float(row[3])
                print("Converted Float:", amount)
            except ValueError:
                print("Invalid string format for conversion to float")
                
            if name in CREDIT_CARD_NAMES:
                category = "Credit Card Payment"
            elif name in SUBSCRIPTION_NAMES:
                category = "Subscriptions"
            elif name in MONEY_TRANSFERS:
                category = "Money Transfers"
            elif name in GROCERIES:
                category = "Groceries"
            elif name in EATING_OUT:
                category = "Eating Out"
            elif name in ENTERTAINMENT:
                category = "Entertainment"
            elif name in HYGIENE:
                category= "Hygiene"
            elif name in MEDICAL_NAMES:
                category = "Medical"
            elif name in GAS_AND_TRANSPORTATION:
                category = "Gas & Transportation"
            elif amount > 0:
                category = "Income"
            else:
                category = 'Other'

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
rows = sofi_bank(file, SUBSCRIPTION_NAMES, 
                    CREDIT_CARD_NAMES, 
                    MEDICAL_NAMES, 
                    HYGIENE, 
                    MONEY_TRANSFERS_OUT, 
                    GROCERIES, 
                    PERSON, 
                    EATING_OUT, 
                    ENTERTAINMENT,
                    GAS_AND_TRANSPORTATION)

pprint(rows)

for row in rows:
    wks.insert_row([row[0], row[1], row[2], row[3]] ,8)
    time.sleep(2)