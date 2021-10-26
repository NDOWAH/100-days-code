# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
int_age = int(age)
days_remaining = 90 - int_age
months_remaining = days_remaining/ 31
years_remaining = months_remaining/12
print(f"You have {days_remaining:.3f} days,{months_remaining:.3f} months,and {years_remaining:.3f} years")