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
    
class C(A):
    def __init__(self):
        super().__init__()
        self.c_attribute = "I am a class C attribute"
    def c_method(self):
        return "This is a method from the class C"  
    
class_b_object = B()
print(class_b_object.a_attribute)  # Accessing inherited attribute from class A
print(class_b_object.b_attribute)  # Accessing own attribute from class B   
print(class_b_object.a_method())    # Calling inherited method from class A
print(class_b_object.b_method())    # Calling own method from class B
class_c_object = C()
print(class_c_object.a_attribute)  # Accessing inherited attribute from class A 
print(class_c_object.c_attribute)  # Accessing own attribute from class C
print(class_c_object.a_method())    # Calling inherited method from class A
print(class_c_object.c_method())    # Calling own method from class C