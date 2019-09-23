class User:
    # Class variables
    company = 'My Bank'

    # constructor
    def __init__(self, fname, lname, email, user_type=None):
        self.first_name = fname
        self.last_name = lname
        self.email = email
        self.user_type = user_type

    # classical setter
    def set_first_name(self, fname):
        self.first_name = fname

    # classical getter
    def get_first_name(self):
        return self.first_name

    def is_privileged(self):
        if self.user_type == 'admin':
            return True
        else:
            return False

    @classmethod
    def present_company(cls):
        print(f'Hey! I work at {cls.company}!')

class Admin(User):
    def __init__(self, fname, lname, email):
        super().__init__(fname, lname, email, user_type='ADMIN')


class Manager(User):
    def __init__(self, fname, lname, email):
        super().__init__(fname, lname, email, user_type='MANAGER')


if __name__ == '__main__':
    u1 = User('Katy', 'Bills', 'kb@example.com')
    u2 = User('John', 'Williams', 'jwilliams2@example.com')

    print(u1.get_first_name())
    u2.set_first_name('Johan')
    print(u2.get_first_name())

    a1 = Admin('Sophie', 'Tyler', 'sophietyler34@example.com')
    print(f'User: {a1.email} privilege status is {a1.is_privileged()}')

    m1 = Manager('Frank', 'Smith', 'f2s3@example.com')
    m1.present_company()
    u1.present_company()