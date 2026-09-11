class A:
    def process(self):
        print("Processing in class A")

class B(A):
    def process(self):
        print("Processing in class B")
        super().process()  # Calls the next class in thee MRO

class C(A):
    def process(self):
        print("Processing in class C")
        super().process()  # Calls the next class in thee MRO

class D(B, C):
    def process(self):
        print("Processing in class D")
        

d = D()
d.process()  # Output: Processing in class D
print(D.__mro__) #Output: (<class 'main.D'>, <class 'main.B'>, <class 'main.C'>, <class 'main_.A'>, <class 'object'>)