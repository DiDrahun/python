list_of_numbers = [1,2,3,4,5,6,7]

sum_of_numbers = 0
for number in list_of_numbers:
    sum_of_numbers = sum_of_numbers + number
print(sum_of_numbers)

max_number = 0
for number in list_of_numbers:
    if number > max_number:
        max_number = number
print(max_number)
