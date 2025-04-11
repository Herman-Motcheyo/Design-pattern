from abc import ABC , abstractmethod

# defines the interface for the payment strategy
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float) -> str:
        pass


# Concrete implementation of the payment strategy for credit card payments
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Paid {amount} using Credit Card."
    
# Concrete implementation of the payment strategy for PayPal payments
class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Paid {amount} using PayPal."
    
# Concrete implementation of the payment strategy for cash payments
class CashPayment(PaymentStrategy):
    def pay(self, amount: float) -> str:
        return f"Paid {amount} using Cash."

# C'est la classe contexte, qui délègue le paiement à une stratégie externe, selon le pattern Strategy.
class ShoppingCart:
    def __init__(self):
        self.items = []  # List of adding articles
        self.payment_strategy = None # Payment strategy

    def add_item(self, item: str):
        self.items.append(item)  # Cette méthode permet d’ajouter un article (représenté comme une chaîne) au panier.


#Ici, on injecte dynamiquement la stratégie de paiement. Cela respecte parfaitement le principe d’inversion de dépendance : le panier ne sait pas comment on paie,
#  il délègue cette logique à un objet stratégie.
    def set_payment_strategy(self, strategy: PaymentStrategy):
        self.payment_strategy = strategy

    def checkout(self) -> str:
        total_amount = sum([10.0 for _ in self.items])  # Assuming each item costs $10
        if not self.payment_strategy:
            return "No payment method selected."
        return self.payment_strategy.pay(total_amount)
    
# Example usage
if __name__ == "__main__":
    cart = ShoppingCart()
    cart.add_item("Item 1")
    cart.add_item("Item 2")

    # Set payment strategy to Credit Card
    cart.set_payment_strategy(CreditCardPayment())
    print(cart.checkout())  

    # Change payment strategy to PayPal
    cart.set_payment_strategy(PayPalPayment())
    print(cart.checkout())  

    # Change payment strategy to Cash
    cart.set_payment_strategy(CashPayment())
    print(cart.checkout())  # Output: Paid 20.0 using Cash.
