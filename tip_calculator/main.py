print("Welcome to Tip Calculator!")
total_bill = float(input("What was your total bill?\n > $"))
tip_percent = (
    float(input("How much percent of tip will you give? 10, 12, 15\n > ")) / 100
)
people = int(input("How many people will split the bill?\n > "))

bill_per_person = (total_bill * tip_percent + total_bill) / people


print("Each person will pay", round(bill_per_person, 2))
