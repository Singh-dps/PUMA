import random

class Booking:
    def __init__(self, event_id, customer_name, tickets_booked):
        self.booking_id = f"BKG-{random.randint(1000, 9999)}" 
        self.event_id = event_id
        self.customer_name = customer_name
        self.tickets_booked = int(tickets_booked)

    def to_dict(self):
        """Helper to save to CSV."""
        return {
            'booking_id': self.booking_id,
            'event_id': self.event_id,
            'customer_name': self.customer_name,
            'tickets_booked': self.tickets_booked
        }

    def __str__(self):
        return f"Booking ID: {self.booking_id} | Event: {self.event_id} | Name: {self.customer_name} | Qty: {self.tickets_booked}"