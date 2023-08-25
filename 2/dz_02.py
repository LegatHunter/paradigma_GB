# Трассировка пути в лабиринте:

# def find_path(maze, start, end):
#     rows = len(maze)
#     cols = len(maze[0])
#     visited = [[False for _ in range(cols)] for _ in range(rows)]

#     def is_valid_move(row, col):
#         return row >= 0 and row < rows and col >= 0 and col < cols and maze[row][col] == '0' and not visited[row][col]

#     def dfs(row, col):
#         if row == end[0] and col == end[1]:
#             return True
        
#         visited[row][col] = True

#         directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
#         for direction in directions:
#             new_row = row + direction[0]
#             new_col = col + direction[1]
#             if is_valid_move(new_row, new_col):
#                 if dfs(new_row, new_col):
#                     return True
        
#         return False

#     return dfs(start[0], start[1])

# maze = [
#     ['0', '1', '0', '0', '0'],
#     ['0', '1', '1', '1', '0'],
#     ['0', '0', '0', '0', '0'],
#     ['0', '1', '1', '1', '0'],
#     ['0', '0', '0', '0', '0']
# ]
# start = (0, 0)
# end = (4, 4)

# if find_path(maze, start, end):
#     print("Путь найден")
# else:
#     print("Путь не найден")



# Разбиение массива на подмассивы:

# def split_array(array, x):
#     subarrays = []
#     current_subarray = []

#     for num in array:
#         if sum(current_subarray) + num <= x:
#             current_subarray.append(num)
#         else:
#             subarrays.append(current_subarray)
#             current_subarray = [num]
    
#     subarrays.append(current_subarray)
#     return subarrays

# array = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# x = 10

# result = split_array(array, x)
# print(result)



# Рекурсивное вычисление чисел Фибоначчи:

# def fibonacci(n):
#     if n <= 0:
#         return None
#     elif n == 1:
#         return 0
#     elif n == 2:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)


# # Пример использования
# n = 10

# result = fibonacci(n)
# print(result)
