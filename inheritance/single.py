class Parent:
    def __init__(self):
        self.parent_attribute = "I am a parent attribute"

    def parent_method(self):
        return "This is a method from the Parent class"
    
class Child(Parent):
    def __init__(self):
        super().__init__()
        self.child_attribute = "I am a child attribute"

    def child_method(self):
        return "This is a method from the Child class"
    
child_object = Child()
print(child_object.child_attribute)  # Accessing child attribute    
print(child_object.parent_attribute)  # Accessing inherited parent attribute
print(child_object.child_method())    # Calling child method
print(child_object.parent_method())   # Calling inherited parent method