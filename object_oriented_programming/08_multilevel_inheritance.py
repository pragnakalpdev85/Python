#multilevel inheritance
class GrandParent:
    def display_grandparent(self):
        print("Grand Parent class")

class Parent(GrandParent):
    def display_parent(self):
        print("Parent class")

class Child(Parent):
    def display_child(self):
        print("Child class")
        
child = Child()
child.display_child()
child.display_parent()
child.display_grandparent()

#overriding methods in multiple levels
#multilevel inheritance
class GrandParent:
    def display(self):
        print("Grand Parent class")

class Parent(GrandParent):
    def display(self):
        print("Parent class")

class Child(Parent):
    def display(self):
        print("Child class")
        
child = Child()
parent = Parent()
grandparent = GrandParent()
child.display()
parent.display()
grandparent.display()
        


