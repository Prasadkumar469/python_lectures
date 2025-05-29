class BankAccount:
    bank_name = "ICICI"

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    
    @classmethod
    def set_bank_name(cls, name):
        cls.bank_name = name

ba1 = BankAccount('ABC', 20000)
print(ba1.owner)
print(ba1.balance)
print(ba1.bank_name)
print(BankAccount.bank_name)
BankAccount.set_bank_name("Axis")
print(ba1.bank_name) # ICICI
print(BankAccount.bank_name)


class Geometry:
    @staticmethod
    def area_of_circle(radius):
        return 3.14 * radius * radius

print(Geometry.area_of_circle(10))
print(Geometry.area_of_circle(20))
    

    


