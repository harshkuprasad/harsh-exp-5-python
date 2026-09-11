class Base:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, my name is {self.name}."


class Derived(Base):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def greet(self):
        base_greeting = super().greet()
        return f"{base_greeting} I am {self.age} years old."


# obj1 = Base("Alice")
obj2 = Derived("Bob", 30)

# print(obj1.greet())
print(obj2.greet())