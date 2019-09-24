# Classical path
import json
import pprint

f1 = open('classical_file.txt', 'w')
f1.write('String one\n')
f1.write('String two\n')
f1.close()

# the Python way
with open('python_way_file.txt', 'w') as f2:
    f2.write('String one\n')
    f2.write('String two\n')

# writing to csv
with open('animals.csv', 'r') as animals_file:
    lines = animals_file.readlines()
    headers = lines[0]
    del lines[0]  # drop headers
    for l in lines:
        print(l.strip('\n'))

with open('addresses.json', 'r') as json_file:
    js = json_file.read()
    js_dict = json.loads(js)
    pprint.pprint(js_dict)


def echo():
    content = input('Provide some string to echo:\n')
    print(content)


if __name__ == '__main__':
    while True:
        echo()
