import sys
bakery = open('bakery.csv', 'a', encoding='utf-8')
bakery.write(f'{sys.argv[1]}\n')
bakery.closed