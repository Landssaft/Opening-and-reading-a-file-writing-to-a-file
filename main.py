import os.path
import os


ST_TITLE = 1
ST_COUNT = 2
ST_INGREDIENTS = 3


cook_book = {}
state = ST_TITLE


with open("write.txt", encoding='utf-8') as f:
    for line in f:
        line = line.strip()
        if not line: continue
        if state == ST_TITLE:
            title = line
            cook_book[title] = []
            state = ST_COUNT
        elif state == ST_COUNT:
            count = int(line)
            state = ST_INGREDIENTS
        else: # if state == ST_INGREDIENTS:
            data = [x.strip() for x in line.split('|')]
            data[1] = int(data[1])
            cook_book[title].append(dict(zip(('ingredient_name', 'quantity', 'measure'), data)))
            count -= 1
            if count == 0:
                state = ST_TITLE


def get_shop_list_by_dishes(person_count, dishes):
    for p in cook_book[title]:
        if p == dishes:
            quantity = quantity * person_count
            print(result)
get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)


def readfile(path: str):
    path = 'D:\directory'
    files_list = os.listdir(path)
    d = {}
    for i in range(1, 3):
        name = f'{i}.txt'
        with open(name, 'r', encoding='utf-8') as f:
            d[name] = [x for x in f.read().splitlines() if x]

    with open('the_source_file.txt', 'w', encoding='utf-8') as file:
        for k, v in sorted(d.items(), key=lambda x: -len([x[1]])):
            file.write(k + '\n')
            file.write(str(len(v)) + '\n')
            file.write('\n'.join(v))
            file.write('\n')