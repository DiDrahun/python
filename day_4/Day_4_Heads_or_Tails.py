import random
test_random_function=random.randint(0, 1)
print(test_random_function)
if test_random_function==0:
    print("Heads")
else:
    print("Tails")

#2
test_random_float_function=random.uniform(0, 2)
print(test_random_float_function)
if test_random_float_function>=1:
    print("Tails")
else:
    print("Heads")    