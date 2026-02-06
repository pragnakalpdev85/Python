#multiple inheritance
class Parent1:
    def display_parent_1(self):
        print("Parent class 1")
        
class Parent2:
    def display_parent_2(self):
        print("Parent class 2")
        
class Child1(Parent1, Parent2):
    def display_child(self):
        print("Child class 1")
        
child = Child1()
child.display_parent_1()
child.display_parent_2()
child.display_child()

#MRO method resolution order
class A:
    def display(self):
        print("Class A")
        
class B(A):
    def display(self):
        print("Class B")
        super().display()
        
class C(A):
    def display(self):
        print("Class C")
        super().display()
        
class D(B,C):
    def display(self):
        print("Class D")
        super().display()
        
d = D()
d.display()