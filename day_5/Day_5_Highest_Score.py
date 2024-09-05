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

#Task 2
from random import randint
big_list = []
for i in range(500):
    big_list.append(randint(1,1000))
print(big_list)

sum_big_list = 0
for number in big_list:
    sum_big_list = sum_big_list + number
print(sum_big_list)

max_big_list = 0
for number in big_list:
    if number > max_big_list:
        max_big_list = number
print(max_big_list)
