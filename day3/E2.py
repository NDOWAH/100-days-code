# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height
if bmi < 18.5:
  print('You are are underweight')
elif bmi < 25:
  print("You have normal weight")
elif bmi < 30:
  print("You are slightly overweight")
elif bmi < 35:
  print("You are obese")
else:
  print("You are clinically obese")



