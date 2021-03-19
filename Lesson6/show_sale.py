import sys

bakery = open('bakery.csv', 'r', encoding='utf-8')
if len(sys.argv) == 1:
    print(bakery.read())
elif len(sys.argv) == 2:
    paragraphs = bakery.readlines()
    for i in range(int(sys.argv[1])-1, len(paragraphs)):
        print(paragraphs[i].removesuffix('\n'))
elif len(sys.argv) == 3:
    paragraphs = bakery.readlines()
    for i in range(int(sys.argv[1])-1, int(sys.argv[2])):
        print(paragraphs[i].removesuffix('\n'))
bakery.closed