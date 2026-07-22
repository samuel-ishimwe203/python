# largest number in list

numbers= [2,3,5,6,8,9,10]
max=numbers[0]

for number in numbers:
    if number > max:
        max= number
print(max)

# odd number in list

numbers= [2,3,5,6,8,9,10]
for number in numbers:
    if number % 2 != 0: 
      print(number)
