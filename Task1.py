import pprint
def my_cook_book():
    with open('recipes.txt', encoding='utf-8')as f:
        cook_book = {}
        for line in f.read().split('\n\n'):
            name, _, *args = line.split('\n')
            cook = []
            for arg in args:
                ingredient_name, quantity, measure = map(lambda x: int(x) if x.isdigit() else x, arg.split(' | '))
                cook.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
            cook_book[name] = cook
    return cook_book
print(my_cook_book())
