def plus_two(number):
    try:
        result = 2 + number
        print(result)
    except TypeError:
        print("число введи")
plus_two(3) 


array = [1, 2, 3, 4, 5]
try:
    index = 7
    value = array[index]
    print(value)
except IndexError:
    print("уехал заграницу")