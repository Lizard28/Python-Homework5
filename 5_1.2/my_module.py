import math
from statistics import mean

def circle() -> float :
   
    radius = float(input("Введите радиус круга: "))
    return math.pi * radius ** 2

def mark() -> float :
   
    grades = list(map(int, input("Введите список оценок [1-5], разделенных пробелом: ").split()))
    if not grades:
        return 0
    return mean(grades)

def sber() -> int:
  
    money = float(input("Введите сумму денег: "))
    price = 317.20
    return int(money // price)
