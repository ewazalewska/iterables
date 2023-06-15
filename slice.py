""" The slice() function returns a slice object.
You can alternately use the following syntax for slicing:
slice[start:stop:step] default: start = 0, stop = the end of the sequence, step = 1 """

numbers = [55, 20, -3, 8, 201]
print(numbers[::-1])                # Output: [201, 8, -3, 20, 55]

letters = "!ldklarsolw6 johljlkeoH"
print(letters[-1::-2])              # Output: Hello world!