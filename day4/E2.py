# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random
rand_int = random.randint(0,len(names))
print(f"{names[rand_int]} will pay the meal today!")



