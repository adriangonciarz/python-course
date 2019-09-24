def returning_constant():
    return 13


def returning_string():
    return 'WOW!'


a = returning_constant
b = locals()["returning_string"]()

x = lambda a: a + 10


def elastic_function(*args):
    for a in args:
        print(a)


def descriptive_function(**kwargs):
    print(f'First name: {kwargs["firstname"]}, last name: {kwargs["lastname"]}')


def filter_divisive_by_three(numbers):
    return list(filter(lambda n: n % 3 == 0, numbers))


if __name__ == '__main__':
    print(a())
    print(b)
    print(x(5))

    elastic_function('cat', 'cow', 1975)
    descriptive_function(firstname='James', lastname='Brown')
    original_list = [1, 3, 13, 14, 16, 18, 21, 190, 303]
    filtered_list = filter_divisive_by_three(original_list)
    print(filtered_list)
