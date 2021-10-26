# A tip means giving a small amount of money to someone who renders service
print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill?: "))
percentage_tip = int(input("What percentage tip would you like to give 10,12 or 15?: "))
number_of_people = int(input("How many people to split the bill?: "))
amount_per_person = (total_bill *(percentage_tip/100) + total_bill) / number_of_people
print(f'Each person will pay ${amount_per_person:.3f}')