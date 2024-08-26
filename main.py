import os.path
import os


def readfile():
    with open("write.txt", encoding='utf-8') as f: #создание словаря
        ST_TITLE = 1
        ST_COUNT = 2
        ST_INGREDIENTS = 3
        cook_book = {}
        state = ST_TITLE
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


def get_shop_list_by_dishes(person_count, dishes): #функция, которая на вход принимает список блюд из cook_book и количество персон для кого мы будем готовить
    for p in dictionary(cook_book[title]):
        if p == dishes:
            quantity = quantity * person_count
            print(dishes)
    get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)
