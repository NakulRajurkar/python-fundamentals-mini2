from datetime import datetime
FILE_NAME="donations.txt"
class Receipt:
    def __init__(self,donor,amount,timestamp=None):
        self.donor=donor
        self.amount=amount
        self.timestamp=timestamp or datetime.now()
    def __str__(self):
        return f"{self.donor} donated $ {self.amount:.2f} on {self.timestamp}"
def save_receipt(receipt):
    with open(FILE_NAME,"a") as file:
        file.write(
            f"{receipt.donor}|{receipt.amount}|{receipt.timestamp.isoformat()}\n"
        )
def load_receipts():
    receipts=[]
    try:
        with open(FILE_NAME,"r")as file:
            for line in file:
                donor,amount,timestamp=line.strip().split("|")
                receipt=Receipt(
                    donor,
                    float(amount),
                    datetime.fromisoformat(timestamp)
                )
                receipts.append(receipt)
    except FileNotFoundError:
        pass
    return receipts
def update_receipt(donor_name, new_amount):
    receipts=load_receipts()
    for receipt in receipts:
        if receipt.donor.lower() == donor_name.lower():
            receipt.amount=new_amount
            break
    else:
        print("Receipt not found.")
        return
    with open(FILE_NAME,"w") as file:
        for receipt in receipts:
            file.write(
                f"{receipt.donor}|{receipt.amount}|{receipt.timestamp.isoformat()}\n"
            )
    print("Receipt updated successfully.")
def delete_receipt(donor_name):
    receipts=load_receipts()
    new_receipts=[
        receipt for receipt in receipts
        if receipt.donor.lower() != donor_name.lower()
    ]
    if len(receipts) == len(new_receipts):
        print("Receipt not found.")
        return
    with open(FILE_NAME,"w")as file:
        for receipt in new_receipts:
            file.write(
                f"{receipt.donor}|{receipt.amount}|{receipt.timestamp.isoformat()}\n"
            )
    print("Receipt deleted successfully.")
def print_report():
    receipts=load_receipts()
    if not receipts:
        print("No donations found.")
        return
    total = sum(receipt.amount for receipt in receipts)
    latest = max(receipts,key=lambda r: r.timestamp)
    print("\n===== TEMPLE DONATION REPORT=====")
    print(f"Total donated : ${total:.2f}")
    print(f"Total receipts: {len(receipts)}")
    print(f"Latest donation: {latest.timestamp.strftime('%Y-%m-%d')}")
print("======================")
r1=Receipt("Nakul",500)
r2=Receipt("Rahul",1000)
r3=Receipt("Amit",750)
save_receipt(r1)
save_receipt(r2)
save_receipt(r3)
print("\nSaved Receipts:")
for receipt in load_receipts():
    print(receipt)
update_receipt("Nakul",800)
delete_receipt("Amit")
print_report()