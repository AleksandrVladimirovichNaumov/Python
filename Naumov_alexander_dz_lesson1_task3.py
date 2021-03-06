# Реализовать склонение слова «процент» для чисел до 20. Например, задаем число 5 — получаем «5 процентов»,
# задаем число 2 — получаем «2 процента». Вывести все склонения для проверки
# list of "процент" forms
list_percentage = [' процент', ' процента', ' процентов']

# using different forms of "процент" depends on number
user_number = int(input('input a number from 1 to 20: '))
if user_number == 1:
    print(user_number, list_percentage[0])
elif user_number in range(2, 5):
    print(user_number, list_percentage[1])
elif user_number in range(5, 21):
    print(user_number, list_percentage[2])
else:
    print('number is not between 1 and 20')

# checking correct work in a cycle
print("_______________________________________________________")
print("checking correct work in a cycle:")
for i in range(1, 21):
    if i == 1:
        print(i, list_percentage[0])
    elif i in range(2, 5):
        print(i, list_percentage[1])
    elif i in range(5, 21):
        print(i, list_percentage[2])
