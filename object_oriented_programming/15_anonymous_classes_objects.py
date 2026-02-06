#anonymous class
obj = type('',(object,),{'name':'John','getname':lambda self : self.name})()
print(obj.getname())