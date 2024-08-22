class Employee:
    raise_amt = 1.05

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    @property
    def full(self):
        # return f'{self.first} {self.last}'
        return '{} {}'.format(self.first, self.last)


emp = Employee('Eldar', 'Bakshi', 1000)
print(emp.full)