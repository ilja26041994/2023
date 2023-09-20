# # Следующие задания требуется решить с привлечением текстовых файлов.
# # Нужно написать функцию, с помощью которой подготовить входной файл, записав
# # в него 100 случайных целых чисел в диапазоне от —50 до +50 по одному на строке.
# # Сформировать выходной файл, преобразовав числа входного файла.
# # 1. Записать выходной файл, добавить к каждому числу последнее число файла.
#
#
# import random
#
# def create_file():
#     with open('file.txt', 'w') as file:
#         for i in range(100):
#             file.write(str(random.randint(-50, 50)) + '\n')
#
# create_file()
#
# def read_file():
#     with open('file.txt', 'r') as file:
#         count = 0
#         listedFile = [int(line) for line in file]
#         print(listedFile)
#         for i in listedFile:
#             count += i
#         print(count)
#
#
# read_file()