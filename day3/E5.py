# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_names = (name1 + name2).upper()
t_count = combined_names.count("T")
r_count = combined_names.count("R")
u_count = combined_names.count("U")
e_count = combined_names.count("E")
sub_count = t_count + r_count + u_count +  e_count

l_count = combined_names.count("L")
o_count = combined_names.count("O")
v_count = combined_names.count("V")
e_count = combined_names.count("E")
sub_count1 = l_count + o_count + v_count + e_count
print(f"Your love score is: {str(sub_count) + str(sub_count1)}")



