class employee:

    def __init__(self, first, last, tax):
        self.first = first
        self.last = last
        self.email = first + last + '@company.com'
        self.tax = tax

    def display(self):
        print('First Name:', self.first)
        print('Last Name:', self.last)
        print('Email:', self.email)
        print('Tax:', self.tax)

    def fullname1(self):
        return '{} {}'.format(self.first, self.last) 

    def fullname2(self):                       # modern version of fullname method 
     return f'{self.first} {self.last}'


emp1 = employee('John', 'Doe', 5000)
emp1.display()
print(emp1.fullname1())

print('\n')

emp2 = employee('rony', 'Dey', 5000)
emp2.display()
print(emp2.fullname2())  

