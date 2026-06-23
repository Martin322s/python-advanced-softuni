from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Tuple

class Order:
    def __init__(self, items: List[Tuple[str, int, float]]):
        self.items = items

    def calculate_total(self) -> float:
        return sum(quantity * price for _, quantity, price in self.items)

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount: float) -> None:
        """Process a payment for the given amount."""
        pass

class CreditCardPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Processing credit card payment for ${amount:.2f}")

class PayPalPayment(PaymentMethod):
    def pay(self, amount: float) -> None:
        print(f"Processing PayPal payment for ${amount:.2f}")

class PaymentProcessor:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def process_payment(self, order: Order) -> None:
        amount = order.calculate_total()
        self.payment_method.pay(amount)

order_obj = Order([
    ("Apple", 2, 1.0),
    ("Banana", 5, 0.5)
])

credit_card_payment = CreditCardPayment()
payment_processor = PaymentProcessor(credit_card_payment)
payment_processor.process_payment(order_obj)