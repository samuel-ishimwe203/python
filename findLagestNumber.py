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

# add number to the list

list= [10,3,4,89,3,3,0,2]

list.append(30)
list.insert(2, 100)
list.remove(3)
print(list)

# remove duplication in list

list2= [2,3,4,1,2,3,4,5,3,4,5,7,8,6,8,5,7]
unique= []
for number in list2:
    if number not in unique:
        unique.append(number)
        unique.sort()
print(unique)
