#If the bill was $150.00, split between 5 people, with 12% tip.
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.:muscle:
#Write your code below this line :point_down:

total_bill=int(input("Enter Total bill - "))
if total_bill < 0:
    print("Total bill cannot be less than 0")
    quit()

number_of_people=int(input("Enter the number of people - "))
if number_of_people <= 0:
    print("Number of people cannot be less or equal to 0")
    quit()

tips=int(input("Enter the tip amount - "))
if tips < 0:
    print("Tips cannot be less than 0")
    quit()

bill_for_each=(total_bill+(total_bill/100*tips))/number_of_people
formatted_bill_for_each=f'{bill_for_each:.2f}'
print(formatted_bill_for_each) 