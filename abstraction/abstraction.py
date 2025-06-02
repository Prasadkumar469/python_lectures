from abc import ABC, abstractmethod

class PaymentProcessor(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

    def balance(self):
        print(20000)

class CreditCardPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Processing credit card payment of ${amount}")

class PayPalPayment(PaymentProcessor):
    def pay(self, amount):
        print(f"Processing PayPal payment of ${amount}")

ccp = CreditCardPayment()
ccp.pay(100)
ccp.balance()
ppp = PayPalPayment()
ppp.pay(200)
ppp.balance()


