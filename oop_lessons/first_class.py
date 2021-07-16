class MyFirstClass:
    pass
# El nombre de las clases en CamelCase según PEP-8

class Point:
    
    def reset(self):
        self.x = 0
        self.y = 0
    

if __name__ == '__main__':
    a = MyFirstClass()
    b = MyFirstClass()

    p1 = Point()
    p2 = Point()
    p1.reset()
    print(p1.x,p1.y)