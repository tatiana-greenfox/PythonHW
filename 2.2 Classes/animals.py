class Animals():
  name = str()
  voice = str()
  type_animal = str()
  weight = 0

  feed = 'нужно накормить'

  def feed_animal(self):
    self.feed = 'накормлена'
    return self.feed

  def print_animal_state(self, state_animal):
    print(f"{self.type_animal} по имени {self.name}:")
    print(f"- {self.feed_animal()}\n- {state_animal}\n- кричит {self.voice}\n")

class Birds():
  pick_eggs = 'нужно собрать яйца'

  def get_pick_eggs(self):
    self.pick_eggs = f'яйца собраны'
    return self.pick_eggs

class Cattle():
  milking = 'нужно подоить'
  grooming = 'нужно постричь'

  def get_milking(self):
    self.milking = 'подоина'
    return self.milking

  def get_grooming(self):
    self.grooming = 'пострижена'
    return self.grooming 

class Geese(Animals, Birds):
  type_animal = 'Гусыня'
  voice = 'га-га'

  def print_animal_state(self):
    super().print_animal_state(self.get_pick_eggs())
  
class Cows(Animals , Cattle):
  type_animal = 'Корова'
  voice = 'мууу...'

  def print_animal_state(self):
    super().print_animal_state(self.get_milking())

class Sheeps(Animals ,  Cattle):
  type_animal = 'Овца'
  voice = 'беее...'

  def print_animal_state(self):
    super().print_animal_state(self.get_grooming())

class Chikens(Animals , Birds):
  type_animal = 'Курица'
  voice = 'куд-кудах'

  def print_animal_state(self):
    super().print_animal_state(self.get_pick_eggs())

class Goats(Animals , Cattle):
  type_animal = 'Коза'
  voice = 'меее...'

  def print_animal_state(self):
    super().print_animal_state(self.get_milking())

class Ducks(Animals , Birds):
  type_animal = 'Утка'
  voice = 'шак-шак'

  def print_animal_state(self):
    super().print_animal_state(self.get_pick_eggs())

def main():
  goose_1 = Geese()
  goose_2 = Geese()
  cow = Cows()
  sheep_1 = Sheeps()
  sheep_2 = Sheeps()
  chicken_1 = Chikens()
  chicken_2 = Chikens()
  goat_1 = Goats()
  goat_2 = Goats()
  duck = Ducks()

  goose_1.name = 'Серая'
  goose_1.weight = 10

  goose_2.name = 'Белая'
  goose_2.weight = 5

  cow.name = 'Манька'
  cow.weight = 100

  sheep_1.name = 'Барашек'
  sheep_1.weight = 50

  sheep_2.name = 'Кудрявая'
  sheep_2.weight = 30

  chicken_1.name = 'Ко-ко'
  chicken_1.weight = 15

  chicken_2.name = 'Кукареку'
  chicken_2.weight = 10

  goat_1.name = 'Рога'
  goat_1.weight = 25

  goat_2.name = 'Копыта'
  goat_2.weight = 35

  duck.name = 'Кряква'
  duck.weight = 35

  animals_list = [goose_1, goose_2, cow, sheep_1, sheep_2, chicken_1, chicken_2, goat_1, goat_2, duck]

  all_weight = 0
  max_weight = 0
  max_type_animal = str()
  max_name = str()
  count = 0
  
  for animal in animals_list:
    all_weight += animal.weight

    while max_weight < animal.weight:
      max_weight = animal.weight
      max_type_animal = animal.type_animal
      max_name = animal.name
      count += 1    
    print(animal.print_animal_state())
  print(f"Максимальный вес в {max_weight} кг у {max_type_animal} по имени {max_name}")
  print(f"Общий вес животных {all_weight}")
main()