class Parent:
    def display(self):
        print("parent class")
        
class Child1(Parent):
    def display_child1(self):
        print("Child class 1")
        
class Child2(Parent):
    def display_child2(self):
        print("Child class 2")
        
class Child3(Parent):
    def display_child3(self):
        print("Child class 3")
        
child1 = Child1()
child2 = Child2()
child3 = Child3()
child1.display()
child1.display_child1()
child2.display_child2()
child3.display_child3()