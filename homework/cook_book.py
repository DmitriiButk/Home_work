import json

with open ('recipe.txt', encoding='utf-8') as file:
    cook_book = {}
    for recipes in file:
        cook_ingridients = int(file.readline())
        cook_list = []
        for i in range(cook_ingridients):
            ingridient_name, quantity, measure = file.readline().strip().split(' | ')
            cook_list.append({
                'ingridient_name': ingridient_name,
                'quantity': quantity,
                'measure': measure
            })
        file.readline()
        cook_book[recipes.strip()]= cook_list
        res = json.dumps(cook_book, ensure_ascii=False,indent=2)
    print(res)

def get_shop_list_by_dishes(dishes, person_count):
    ingredients = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            if ingredients.get(ingridient['ingridient_name']):
                ingredients[ingridient['ingridient_name']]['quantity'] += int(ingridient['quantity']) * person_count
            else:
                ingredients[ingridient['ingridient_name']] = {'measure': ingridient['measure'],
                                                           'quantity': int(ingridient['quantity']) * person_count}
    return ingredients

print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))


