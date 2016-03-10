def func(x):
    return x + 10

class Demo:
    def func(self, x):
        return func(x) + self.__value

    def __init__(self, value):
        self.__value = value

demo = Demo(2)
result = demo.func(10)

print(result)
