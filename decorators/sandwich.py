
def bread(func):
    def wrapper(food):
        print("</''''''\>")
        func(food)
        print("<\______/>")
    return wrapper

def ingredients(func):
    def wrapper_ingredients(food):
        print('#tomatoes#')
        func(food)
        print('~salad~')
    return wrapper_ingredients

@bread
@ingredients
def sandwich(food='--ham--'):
    print(food)


if __name__ == "__main__":
    sandwich("queso")
