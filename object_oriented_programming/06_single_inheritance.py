#single inheritance
class Parent:
    def display_parent(self):
        print("Parent class")
        
class Child(Parent):
    def display_child(self):
        print("Child class")
        
child = Child()
child.display_child()
child.display_parent()