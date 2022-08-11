fruits = ["apple", "pear", "orange"]

def make_pie(index):
    fruit: str = ""
    try:
        fruit = fruits[index]
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit + " pie")



make_pie(0)