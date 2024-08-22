import os.path
import os


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


def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['product'] in result:
                    result[consist['product']]['quantity'] += consist['quantity'] * person_count
                else:
                    result[consist['product']] = {'measure': consist['measure'],'quantity': (consist['quantity'] * person_count)}
        else:
            print('В книге нет этого блюда')
    print(result)
get_shop_list_by_dishes(['Омлет', 'Омлет'], 2)


def read_files(directory):
    directory = "D:\directory"
    for root, dirs, files in os.walk(directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            with open(file_path, "r") as file:

    def count_lines(directory, chunk_size=1 << 13):
        with open(directory,'w') as file:
            return sum(chunk.count('\n')
                       for chunk in iter(lambda: file.read(chunk_size), ''))
                       f.write('D:\directory\the_source_file.txt')
