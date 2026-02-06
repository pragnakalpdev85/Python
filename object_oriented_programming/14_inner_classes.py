class Outer:
   def __init__(self):
       self.name = "Outer class"
      
   class Inner:
       def __init__(self):
           self.name = "Inner class"

outer = Outer()
inner = outer.Inner()

print(outer.name)
print(inner.name)

#multiple inner classes
class Outer:
    def __init__(self):
        self.inner1 = self.Inner1()
        self.inner2 = self.Inner2()
        
    class Inner1:
        def display(self):
            print("Inner class 1")
        
    class Inner2:
        def display(self):
            print("Inner class 2")
            
outer = Outer()
outer.inner1.display()
outer.inner2.display()

#multilevel inner class
class Organization:
   def __init__(self):
      self.inner = self.Department()

   class Department:
      def __init__(self):
         self.innerTeam = self.Team1()

      def displayDep(self):
         print("Department class")

      class Team1:
         def displayTeam(self):
            print("Team 1 of the department")
            
organization = Organization()
organization.inner.displayDep()
organization.inner.innerTeam.displayTeam()
