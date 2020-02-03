#Задания 1-2
def main():
  while True:
    try:
      operation, a, b = input('Введите последовательно через пробел одну из арифметических операций (+, -, /, *) и два числа:').split()
    except ValueError as e:
      print(f"Ошибка: {e}\nВозможно вы ввели недостаточно данных, либо забыли поставить пробелы между операндами")
    else:
      assert operation in ['+', '-', '/', '*'], 'Ошибка! Операция введена не верно!'
      try:
        a, b = int(a), int(b)
      except ValueError as e:
        print(f"Ошибка: {e}\nПроверьте правильно ли вы ввели последние два числа")
      else:
        arithmetic_operations(operation, a , b)
    print()

def arithmetic_operations(operation, a, b):
  if (a < 0) or (b < 0):
    print('Вы ввели отрицательное число!')
  elif operation == '+':
    print(f"Сумма введенных чисел равна: {a + b}")
  elif operation == '-':
    print(f"Разность введенных чисел равна: {a - b}")
  elif operation == '*':
    print(f"Произведение введенных чисел равно: {a * b}")
  elif operation == '/':
    try:
      print(f"Частное введенных чисел равно: {a / b}")
    except ZeroDivisionError:
      print('Ошибка! Попытка деления на ноль') 

main()