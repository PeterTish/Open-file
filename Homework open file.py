def recipe(file_name):
    cook_book = {}

    with open(file_name) as file:
        for line in file:
            dish_name = line.strip()
            ingr_quantity = int(file.readline().strip())

            ingridient_list = []
            for ingr in range(ingr_quantity):
                ingridient_name, quantity, measure  = file.readline().strip().split('|')
                ingridient_dict = {'ingridient_name': ingridient_name, 'quantity': quantity, 'measure': measure}
                ingridient_list.append(ingridient_dict)
            cook_book[dish_name] = ingridient_list
            file.readline()

    return cook_book



print(recipe('Task №1.txt'))


def get_shop_list_by_dishes(dishes, person_count):
    shopping_dict = {}
    for dish in dishes:

        if dish in recipe('Task №1.txt'):

            for ingridients in recipe('Task №1.txt')[dish]:

                keys = ingridients['ingridient_name']
                if keys in shopping_dict:
                    shopping_dict[keys]['quantity'] += int(ingridients['quantity']) * person_count
                else:
                    shopping_dict[keys] = {'measure': ingridients['measure'], 'quantity': int(ingridients['quantity']) * person_count}

    return shopping_dict


print(get_shop_list_by_dishes(['Омлет', 'Фахитос', 'Запеченный картофель'], 2))
























