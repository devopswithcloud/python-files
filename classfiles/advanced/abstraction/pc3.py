from abc import ABC,abstractmethod

class Payment(ABC):
    @abstractmethod
    def pay(self,amount):
        pass

class CreditCard(Payment):
    def pay(self,amount):
        print(f"paid{amount} via credit card")

class PayPal(Payment):
    def pay(self,amount):
        print(f"paid{amount} via pay pal")


def process_payment(payment:Payment,amount:float):
    payment.pay(amount)

payment1 = CreditCard()
payment2 = PayPal()

process_payment(payment1,500)
process_payment(payment2,100)
