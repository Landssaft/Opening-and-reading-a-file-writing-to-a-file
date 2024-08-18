with open('write.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        recepie_name = i.strip()
        ingredients_count = file.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recepie = file.readline().strip().split(' | ')
            product, quantity, word = recepie
            ingredients.append({'product': product, 'quantity': quantity, 'measure': word})
        file.readline()
    cook_book[recepie_name] = ingredients


def get_shop_list_by_dishes(person_count, **dishes):
    for p in ingredients:
        if p == dishes:
            quantity = quantity * person_count
            print(dishes)
print(cook_book)


with open('1.txt', 'rt', encoding='utf-8') as f_1:
    def count_lines('1.txt', chunk_size=1 << 13):
        with open('1.txt') as file:
            return sum(chunk.count('\n')
                       for chunk in iter(lambda: file.read(chunk_size), ''))


with open('2.txt', 'rt', encoding='utf-8') as f_1:
    def count_lines('2.txt', chunk_size=1 << 13):
        with open('2.txt') as file:
            return sum(chunk.count('\n')
                       for chunk in iter(lambda: file.read(chunk_size), ''))


with open('3.txt', 'rt', encoding='utf-8') as f_1:
    def count_lines('3.txt', chunk_size=1 << 13):
        with open('3.txt') as file:
            return sum(chunk.count('\n')
                       for chunk in iter(lambda: file.read(chunk_size), ''))


f.write('1.txt','2.txt','3.txt')