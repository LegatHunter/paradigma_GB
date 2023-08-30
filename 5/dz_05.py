# Задача 1: Напишите программу, которая находит все простые числа в заданном диапазоне.

# a = int(input("Введите начальное число диапазона: "))
# b = int(input("Введите конечное число диапазона: "))

# if a < 1:
#     print("Число должно быть больше 0")
# else:
#     primes = []
#     for i in range(a, b+1):
#         if i > 1:
#             is_prime = True
#             for j in range(2, int(i**0.5) + 1):
#                 if i % j == 0:
#                     is_prime = False
#                     break
#             if is_prime:
#                 primes.append(i)

#     print("Простые числа в заданном диапазоне:")
#     print(primes)

# Задача 2: Напишите программу, которая сортирует список чисел методом сортировки слиянием.

# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i]< right[j]:
#                 nums[k]=left[i]
#                 i+=1
#             else:
#                 nums[k] = right[j]
#                 j+=1
#             k+=1
#         while i < len(left):
#             nums[k] = left[i]
#             i+=1
#             k+=1
#         while j < len(right):
#             nums[k] = right[j]
#             j+=1
#             k+=1

# a = [2, 4, 6, 1 ,8, 14, 546, 564, 2, 12, 0, 12, 45, 78]
# merge_sort(a)
# print(a)