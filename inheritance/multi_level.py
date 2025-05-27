class A:
    def __init__(self):
        self.a_attribute = "I am a class A attribute"

    def a_method(self):
        return "This is a method from the class A"
    
class B(A):
    def __init__(self):
        super().__init__()
        self.b_attribute = "I am a class B attribute"

    def b_method(self):
        return "This is a method from the class B"
    
class C(B):
    def __init__(self):
        super().__init__()
        self.c_attribute = "I am a class C attribute"

    def c_method(self):
        return "This is a method from the class C"
    
c_class_object = C()
print(c_class_object.a_attribute)  # Accessing inherited attribute from class A
print(c_class_object.b_attribute)  # Accessing inherited attribute from class B
print(c_class_object.c_attribute)  # Accessing own attribute from class C
print(c_class_object.a_method())    # Calling inherited method from class A
print(c_class_object.b_method())    # Calling inherited method from class B
print(c_class_object.c_method())    # Calling own method from class C
    
