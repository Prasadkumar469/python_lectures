class BankAccount:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        print('name getter method is called')
        return self._name
    
    @name.setter
    def name(self, value):
        print('name setter method is called')
        if len(value) > 20:
            raise Exception('name is more than 20 characters')
        self._name = value

ba = BankAccount('ddfdfdfdfdfdfdfdfdfdfdfdfdf')
print(ba.name)

