# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
cummulative_bill = 0
if size == "S":
  cummulative_bill += 15
  if add_pepperoni == "Y":
      cummulative_bill += 2
      print(f"Your final bill is ${cummulative_bill}")
elif size == "M":
  cummulative_bill += 20
  if add_pepperoni == "Y":
    cummulative_bill += 3
    print(f"Your final bill is ${cummulative_bill}")
elif size == "L":
  cummulative_bill += 25
  if add_pepperoni == "Y":
    cummulative_bill += 3
    print(f"Your final bill is ${cummulative_bill}")
elif extra_cheese == "Y":
  cummulative_bill += 1
  print(f"Your final bill is ${cummulative_bill}")
else:
  print(f"Your final bill is ${cummulative_bill}")