# Way of creating ultidimensional list

matrix_list = [[[], [], []], [[], [], []], [[], [], []]]
matrix_list[1][1] = "pen"

for el in matrix_list:
    print(el)

""" 
[[], [], []]
[[], 'pen', []]
[[], [], []] 
"""