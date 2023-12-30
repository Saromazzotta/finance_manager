import csv
import gspread
import time
from pprint import pprint
from expenses import SUBSCRIPTION_NAMES, CREDIT_CARD_NAMES, MEDICAL_NAMES, HAIRCUT, MONEY_TRANSFERS_OUT, GROCERIES, PERSON



MONTH = "december"

file = f"sofi_{MONTH}.csv"

transactions = []

def sofi_bank(file, SUBSCRIPTION_NAMES, CREDIT_CARD_NAMES, MEDICAL_NAMES, HAIRCUT, MONEY_TRANSFERS, GROCERIES):

    with open(file, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            date = row[0]
            name = row[1] 
            try:
                amount = row[3]
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
            else:
                category = 'Other'

            transaction = ((date, name, category, amount))
            transactions.append(transaction)
        return transactions

sa = gspread.service_account()
sh = sa.open("Personal Finances")

wks = sh.worksheet(f"{MONTH}")

rows = sofi_bank(file, SUBSCRIPTION_NAMES, CREDIT_CARD_NAMES, MEDICAL_NAMES, HAIRCUT, MONEY_TRANSFERS_OUT, GROCERIES)

pprint(rows)

# for row in rows:
#     wks.insert_row([row[0], row[1], row[2], row[3]] ,8)
#     time.sleep(2)
    
# wks.insert_row([1,2,3], 10)