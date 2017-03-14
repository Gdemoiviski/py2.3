import json

def meny_recipe(recipe):
    cook_book_entry = {}
    dish_name = recipe[0].lower().strip()
    cook_book_entry[dish_name] = []
    ingredients_quantity = int(recipe[1])
    for index in range(ingredients_quantity):
        ingredient = recipe[index+2].split('|')
        cook_book_entry[dish_name].append({"ingredient_name": ingredient[0].lower().strip(), "quantity": int(ingredient[1]), "measure": ingredient[2].lower().strip()})
    return cook_book_entry

def get_recipes():
    cook_book ={}
    with open('meny.json', encoding='UTF8') as recipes:
        recipe = []
        for entry in recipes:
            entry = entry.strip()
            if entry == '':
                cook_book.update(meny_recipe(recipe))
                recipe = []
            else:
                recipe.append(entry)
        cook_book.update(meny_recipe(recipe))
        print(cook_book)
    return cook_book

# Неизменная часть

def get_shop_list_by_dishes(cook_book, dishes, person_count):
    shop_list = {}

    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item["quantity"] *= person_count
            if new_shop_list_item["ingredient_name"] not in shop_list:
                shop_list[new_shop_list_item["ingredient_name"]] = new_shop_list_item
            else:
                shop_list[new_shop_list_item["ingredient_name"]]["quantity"] += new_shop_list_item["quantity"]
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        print("{ingredient_name} {quantity} {measure}".format(**shop_list_item))


def create_shop_list():
    cook_book = get_recipes()
    person_count = int(input("Введите количество человек:"))
    dishes = input("Введите блюда в расчете на одного человека (через запятую):").lower().split(', ')
    shop_list = get_shop_list_by_dishes(cook_book, dishes, person_count)
    print_shop_list(shop_list)


create_shop_list()