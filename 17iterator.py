#iterator
str1 = "hello, i am het"
it = iter(str1)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))

#creating an iterator
class EvenIterator:
    def __iter__(self):
        self.a = 2
        return self
        
    
    def __next__(self):
        x = self.a
        self.a += 2
        return x
    
evens = EvenIterator()
eveniter = iter(evens)
print(next(eveniter))
print(next(eveniter))
print(next(eveniter))
print(next(eveniter))
print(next(eveniter))
print(next(eveniter))
