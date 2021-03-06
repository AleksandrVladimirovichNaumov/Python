import random

# max number for generator
max_number = random.randint(2, 50)
odd_numbers = (n for n in range(1, max_number + 1, 2))
for i in odd_numbers:
    print(f'next(odd_number_{max_number + 1})\n{i}')
# checking type of generator
print(type(odd_numbers))
