from abc import ABC, abstractmethod

# Abstract Class
class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Credit Card Payment
class CreditCardPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using Credit Card")


# UPI Payment
class UPIPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using UPI")


# Net Banking Payment
class NetBankingPayment(Payment):

    def pay(self, amount):
        print(f"Paid {amount} using Net Banking")


# Using abstraction
def make_payment(payment_method, amount):
    payment_method.pay(amount)


# Objects
c = CreditCardPayment()
u = UPIPayment()
n = NetBankingPayment()

make_payment(c, 1000)
make_payment(u, 500)
make_payment(n, 2000)