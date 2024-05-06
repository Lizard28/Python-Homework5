import random

def shuffle_list(list1): 
    list1_str = input("Введите список элементов, разделёных пробелом: ")
    list1 = list1_str.split(" ")
    random.shuffle(list1)
    return list1

shuffled_list = shuffle_list([])

print(shuffled_list)
