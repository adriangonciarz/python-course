# Classic Hello world
print('Hello world!')

# Strings
first_name = 'Adrian'
last_name = 'Gonciarz'
# Formatting
description = f'My name is {first_name} {last_name}'
description2 = 'My name is {} {}'.format(first_name, last_name)
long_string = """
It is possible to write strings in this manner.
Sometimes it's usable to write multi-line strings, especially when dealing with preformatted data
such as HTML or some other file-like strings.
"""

print(description)
print(description2)
print(long_string)

# Numeric variables
integer_variable = 69
float_var = 42.42
decimal_var = .333
big_number = 1_000_000

print(integer_variable + big_number + float_var + decimal_var)

# Casting data types
int_to_str = str(integer_variable)
print(type(int_to_str))
integer_as_string = '6782'
# print(22 + integer_as_string) - it will not work

str_to_int = int(integer_as_string)
print(22 + str_to_int)

# Other data types
my_list = [1, 2, 3, 4, 5, 6]
my_list_mixed = [22, 34.7, 'flowers']
print(my_list[2])
my_list.append(127)
print(my_list)


my_dictionary = {
    'a': 1,
    'b': 2,
    'c': 'dog'
}
print(my_dictionary['c'])
my_dictionary['d'] = 'cat'

my_tuple = ('bike', 'car', 'motorcycle')
print(my_tuple[2])