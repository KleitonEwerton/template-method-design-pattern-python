from abc import ABC, abstractmethod
# some function
class OrderProcessor(ABC):
    """Template method defining steps to process an order."""

    def process_order(self, order):
        """Template method: defines skeleton of order processing."""
        self.validate_order(order)
        self.charge_payment(order)
        self.package(order)
        self.ship_or_deliver(order)
        self.send_notification(order)

    # Common steps with default implementations
    def validate_order(self, order):
        print(f"Validating order {order['id']} for {order['item']}")

    def charge_payment(self, order):
        print(f"Charging payment for order {order['id']}: ${order['price']:.2f}")

    def package(self, order):
        print(f"Packaging item for order {order['id']}")

    def send_notification(self, order):
        print(f"Sending notification for order {order['id']} to {order.get('customer_email', 'unknown')}")

    # Steps that differ between order types
    @abstractmethod
    def ship_or_deliver(self, order):
        pass


class PhysicalProductOrderProcessor(OrderProcessor):
    def ship_or_deliver(self, order):
        self.print_shipping_label(order)
        print(f"Order {order['id']} shipped via {order.get('carrier', 'standard carrier')}")

    def print_shipping_label(self, order):
        print(f"Printing shipping label for {order['address']}")


class DigitalProductOrderProcessor(OrderProcessor):
    def package(self, order):
        # override packaging for digital products
        print(f"Preparing digital download package for order {order['id']}")

    def ship_or_deliver(self, order):
        print(f"Delivering download link for order {order['id']} to {order.get('customer_email')}")


class SubscriptionOrderProcessor(OrderProcessor):
    def charge_payment(self, order):
        # Subscriptions may involve recurring billing setup
        print(f"Setting up recurring billing for order {order['id']} - ${order['price']:.2f} per {order.get('interval', 'month')}")

    def ship_or_deliver(self, order):
        print(f"Activating subscription for order {order['id']} (plan: {order.get('plan', 'standard')})")


if __name__ == '__main__':
    physical_order = {
        'id': 'P1001',
        'item': 'Wireless Mouse',
        'price': 29.99,
        'address': '123 Main St, Springfield',
        'customer_email': 'alice@example.com',
        'carrier': 'FastShip'
    }

    digital_order = {
        'id': 'D2001',
        'item': 'E-book: Learn Python',
        'price': 9.99,
        'customer_email': 'bob@example.com'
    }

    subscription_order = {
        'id': 'S3001',
        'item': 'Music Streaming',
        'price': 4.99,
        'customer_email': 'carol@example.com',
        'plan': 'premium',
        'interval': 'month'
    }

    print('Processing physical product order:\n')
    PhysicalProductOrderProcessor().process_order(physical_order)

    print('\nProcessing digital product order:\n')
    DigitalProductOrderProcessor().process_order(digital_order)

    print('\nProcessing subscription order:\n')
    SubscriptionOrderProcessor().process_order(subscription_order)
