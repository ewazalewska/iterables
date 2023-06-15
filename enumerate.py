# The enumerate() function returns a tuple containing a count and the values
fruits = ['apple', 'banana', 'orange', 'strawberry']

num = 1
for element in fruits:
    print(num, element)
    num +=1

print('--------')

for n, element in enumerate(fruits):
    print(n,element)

print('--------')

for n, element in enumerate(fruits,1):
    print(n,element)

print('xxxxxxxx')

print(list(enumerate(fruits)))
print(enumerate(fruits))

""" 
1 apple
2 banana
3 orange
4 strawberry
--------
0 apple
1 banana
2 orange
3 strawberry
--------
1 apple
2 banana
3 orange
4 strawberry
xxxxxxxx
[(0, 'apple'), (1, 'banana'), (2, 'orange'), (3, 'strawberry')]
<enumerate object at 0x000002A1D5C81E00> 
"""