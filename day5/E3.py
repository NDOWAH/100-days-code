#Write your code below this row 👇
total = 0
for number in range(1, 101, 2):
  total += number
print(total)

# Method 2
total = 0
for number in range(1,101):
  if number % 2 == 0:
      total += number
print(total)