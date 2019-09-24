# Classical path
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
