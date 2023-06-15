# Diferences between lists and tuples

# Synax
list = [1, 2, 3]
tuple = (1, 2, 3)

# List is mutable, tuple is not
list[1]=50
print(list)
# tuple[1]=50 --> TypeError: 'tuple' object does not support item assignment

# Tuple can be used as a key in a dictionary
dict_tuple = {tuple: 1}
# dict_list = {list: 1} --> TypeError: unhashable type: 'list'

# List needs more memory