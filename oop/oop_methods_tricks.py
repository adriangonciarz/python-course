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


if __name__ == '__main__':
    print(a())
    print(b)
    print(x(5))

    elastic_function('cat', 'cow', 1975)
    descriptive_function(firstname='James', lastname='Brown')
