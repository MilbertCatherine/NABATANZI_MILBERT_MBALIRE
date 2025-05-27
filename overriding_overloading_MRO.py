# Base class for demonstrating overriding
class Animal:
    def speak(self):
        print("Animal speaks")

# Derived class overriding speak()
class Dog(Animal):
    def speak(self):
        print("Dog barks")  # This overrides Animal's speak()

# Demonstrating method overloading in Python (using default args)
class Calculator:
    def add(self, a, b=0, c=0):
        return a + b + c

# MRO Example with multiple inheritance
class A:
    def do_something(self):
        print("A's method")

class B(A):
    def do_something(self):
        print("B's method")

class C(A):
    def do_something(self):
        print("C's method")

class D(B, C):  # Multiple inheritance
    pass

# === Run Demo ===
print("=== Method Overriding ===")
animal = Animal()
dog = Dog()
animal.speak()  # Output: Animal speaks
dog.speak()     # Output: Dog barks (overridden)

print("\n=== Method Overloading (Python-style) ===")
calc = Calculator()
print(calc.add(5))           # 5 + 0 + 0 = 5
print(calc.add(5, 3))        # 5 + 3 + 0 = 8
print(calc.add(5, 3, 2))     # 5 + 3 + 2 = 10

print("\n=== Method Resolution Order (MRO) ===")
d = D()
d.do_something()             # Output: B's method (MRO: D -> B -> C -> A)
print("MRO of class D:", [cls.__name__ for cls in D.__mro__])
