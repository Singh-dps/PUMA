import csv

class Event:
    def __init__(self, event_id, name, total_tickets, price):
        self.event_id = event_id
        self.name = name
        self.total_tickets = int(total_tickets)
        # Initially, available equals total
        self.available_tickets = int(total_tickets)
        self.price = float(price)

    def update_availability(self, quantity, operation='book'):
        """Updates ticket count based on booking or cancellation."""
        if operation == 'book':
            self.available_tickets -= quantity
        elif operation == 'cancel':
            self.available_tickets += quantity
    
    def to_dict(self):
        """Helper to save to CSV."""
        return {
            'event_id': self.event_id,
            'name': self.name,
            'total_tickets': self.total_tickets,
            'available_tickets': self.available_tickets,
            'price': self.price
        }

    def __str__(self):
        return f"ID: {self.event_id} | {self.name} | Avail: {self.available_tickets}/{self.total_tickets} | Price: ${self.price}"