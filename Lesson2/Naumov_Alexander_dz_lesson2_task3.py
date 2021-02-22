# *(вместо задачи 2) Решить задачу 2 не создавая новый список (как говорят, in place).
# Эта задача намного серьёзнее, чем может сначала показаться.

my_list = ['в', '   5 ', 'часов', '17', ' минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
print(f'initial list:\n{my_list}\n')

# variable for + or - before number
symbol = ''

# formatting all list items in a cycle
for index, i in enumerate(my_list):
    i = i.lstrip()  # delete all spaces before value
    i = i.rstrip()  # delete all spaces after value
    # checking + or - before number. if yes delete it from i and save in var symbol
    if i[0] == "+" or i[0] == "-":
        symbol = i[0]
        i = i[1:]
    # checking if it is a number
    if i.isdigit():
        # adding 0 before number if it is 1 symbol
        if len(i) < 2:
            i = i.zfill(2)
        my_list[index] = '"' + symbol + i + '"'  # adding back a symbol (or empty symbol) and ""
    else:
        # if not a number just add deleted symbol or empty symbol
        i = symbol + i
    symbol = ''  # making symbol empty for next cycle
print(f'list after modification:\n{my_list}\n')
print(f'joined string:\n{" ".join(my_list)}')
