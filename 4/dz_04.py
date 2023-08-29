# Рекурсивная сумма: Напишите рекурсивную функцию, которая вычисляет сумму всех чисел от 1 до n. Например, для n = 5 результат должен быть 1 + 2 + 3 + 4 + 5 = 15.

# def recursive_sum(n):
#     if n == 1:
#         return 1
#     else:
#         return n + recursive_sum(n-1)

# n = int(input("Введите число n: "))
# result = recursive_sum(n)
# print("Сумма чисел от 1 до", n, ":", result)

# Факториал: Напишите рекурсивную функцию для вычисления факториала числа n. Факториал числа n обозначается как n! и равен произведению всех положительных целых чисел от 1 до n.

# def recursive_factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n * recursive_factorial(n-1)

# n = int(input("Введите число n: "))
# result = recursive_factorial(n)
# print("Факториал числа", n, ":", result)

# Фибоначчи через рекурсию: Напишите рекурсивную функцию для вычисления числа Фибоначчи с индексом n. Напоминаю, что последовательность Фибоначчи определяется как: F(0) = 0, F(1) = 1 и F(n) = F(n-1) + F(n-2) для n > 1.

# def recursive_fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)

# n = int(input("Введите индекс числа Фибоначчи: "))
# result = recursive_fibonacci(n)
# print("Число Фибоначчи с индексом", n, ":", result)

# Функция-редуктор: Функция-редуктор: Напишите функцию-редуктор (или функцию свертки), которая принимает начальное значение и список чисел, а затем возвращает произведение всех чисел в списке. Используйте эту функцию для вычисления произведения чисел в списке.

# def reduce_multiply(initial_value, number_list):
#     result = initial_value
#     for num in number_list:
#         result *= num
#     return result

# numbers = [1, 2, 3, 4, 5]
# product = reduce_multiply(1, numbers)
# print("Произведение чисел в списке:", product)

# Создайте функцию, которая принимает некоторое число n и возвращает функцию, которая прибавляет n к своему аргументу. Продемонстрируйте использование этой функции-замыкания.

# def add_n(n):
#     def add_number(x):
#         return x + n
#     return add_number

# add_5 = add_n(5)
# result = add_5(10)
# print(result)

# add_10 = add_n(10)
# result = add_10(5)
# print(result)

# Напишите функцию-редуктор, которая принимает список строк и возвращает строку, состоящую из объединенных элементов списка через запятую. Например, для списка ["apple", "banana", "cherry"] результат должен быть "apple, banana, cherry".

# def reduce_strings(lst):
#     return ", ".join(lst)

# strings = ["apple", "banana", "cherry"]
# result = reduce_strings(strings)
# print(result)

# Напишите функцию, которая будет генерировать бесконечную последовательность простых чисел. Используйте ленивые вычисления, чтобы генерировать только те числа, которые действительно нужны.

# def is_prime(n):
#     if n <= 1:
#         return False
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def generate_primes():
#     num = 2
#     while True:
#         if is_prime(num):
#             yield num
#         num += 1

# primes = generate_primes()
# for i in range(10):
#     print(next(primes))