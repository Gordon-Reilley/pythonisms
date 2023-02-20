#  LAB: 42 Pythonisms

## Description
Practice Pythonisms using object methods and python generators.

## Pythonisms 
__init__(self, data): This is the class constructor. It is called when a new instance of the Pythonisms class is created. It takes one argument, data, which is used to initialize the data attribute of the object.

__iter__(self): This method makes the object iterable. It returns an iterator that allows you to loop over the items in the data attribute of the object.

__len__(self): This method returns the length of the object. It is called when you use the len() function on an instance of the Pythonisms class.

__getitem__(self, index): This method allows you to access items in the data attribute of the object using square bracket notation, for example p[0] will return the first item in the data attribute of the Pythonisms object p.

__setitem__(self, index, value): This method allows you to set items in the data attribute of the object using square bracket notation, for example p[0] = 4 will set the first item in the data attribute of the Pythonisms object p to 4

## Generator
multiply(a, b): This function takes two integer arguments a and b. It uses a while loop to generate a series of values by multiplying b by the integers from 1 to a. It uses the yield keyword to create a generator that generates these values one at a time.

line_by_line(item): This function takes a list item as an argument. It uses a while loop to generate a series of values by yielding the first element of the list, and then removing it from the list using the pop() method. This allows you to iterate over the list one element at a time, without modifying the original list. The function creates a generator that generates these values one at a time.