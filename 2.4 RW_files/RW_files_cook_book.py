#Задание 1. 
def get_dictionary_cook_book():
  recipes_dict = {}

  with open('recipes.txt', encoding = 'utf-8') as cook_book:          
    #читаем файл по три записи
    while True:
      #считываем название блюда
      dish_name = cook_book.readline().strip()
      if not dish_name:
        break
      #считываем кол-во блюд
      count_ingredients = cook_book.readline().strip()
      counter = 0 
      ingredients_list = []
      while counter <= int(count_ingredients):
        #считываем список ингредиентов
        ingredients = cook_book.readline().strip()
        ingredients_list.append(ingredients)
        counter += 1
      ingredients_list.pop()

      key = dish_name
      recipes_dict[key] = ingredients_list
    
    #формируем словарь в указанном виде
    for key, values in recipes_dict.items():
      ingredient_list = []
      ingredient_list_2 = []

      for value in values:
        value = value.split(' | ')  
        ingredient_list.append(value)

      for value in ingredient_list:
        ingredient_dict = {
          'ingredient_name': value[0],
          'quantity': value[1],
          'measure': value[2]
        }

        ingredient_list_2.append(ingredient_dict)
      recipes_dict[key] = ingredient_list_2
    return recipes_dict

#Задание 2.
def get_shop_list_by_dishes(dishes, person_count):
  recipes_dict = get_dictionary_cook_book()
  ingredient_dict = {}
  #count_dishes = 0
  
  for key, values in recipes_dict.items():
    for value in dishes:
      count_dishes = dishes.count(value)

      if key == value:
        for ingredient in values:
          quantity = int(ingredient['quantity']) * person_count * count_dishes

          count_ingredient_dict = {
            'measure': ingredient['measure'], 
            'quantity': quantity
          }

          name_ingredient = ingredient['ingredient_name']
          ingredient_dict[name_ingredient] = count_ingredient_dict
  print(ingredient_dict)

def main():
  print(get_dictionary_cook_book() , '\n')
  get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
  
main()