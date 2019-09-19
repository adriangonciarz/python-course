# Classic Hello world
import random

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

### Control Statements
a = 10
b = 20

if a > b:
    print('A is greater than B!')
elif a < b:
    print('B is greater than A!')
else:
    print('A and B are equal!')

# Ternary Operator
threshold = 100
value = 200

status = 'green' if value <= threshold else 'red'
print('The status is: ' + status)

# Case Switch
bands = ['Led Zeppelin', 'Dire Straits', 'Deep Purple', 'The Cure']
random_band = random.choice(bands)

if random_band == 'Led Zeppelin':
    print('I wanna be your backdoor man!')
elif random_band == 'Dire Straits':
    print('You gotta move this refrigerator.')
elif random_band == 'Deep Purple':
    print('Nobody\'s gonna take my car, it\'s gonna break the speed of sound.')
elif random_band == 'The Cure':
    print("It's Friday I'm in love")

# Loop for N times
for _ in range(4):
    print('Hey Ho, let\'s go!')

# Loop over array
for band in bands:
    print(band.upper())

# loop over dictionary
bands_songs_map = {'Led Zeppelin': 'Black Dog', 'Dire Straits': 'Sultans Of Swing', 'Deep Purple': 'Child in Time',
                   'The Cure': 'Boys don\'t cry'}
for band, song in bands_songs_map.items():
    print(f'Do you know this awesome song "{song}" by {band}?!')

# Loop while
i = 0
while i < 10:
    print(i)
    i += 2

# List comprehension
old_list = list(range(20))  # This is equivalent to old_list = [1, 2, 3, 4....19, 20]
new_list = [i ** 2 for i in old_list]
print(new_list)

new_list_only_even = [i ** 2 for i in old_list if i % 2 == 0]
print(new_list_only_even)

