import csv
import os
import pandas as pd
import matplotlib.pyplot as plt
from event_class import Event
from booking_class import Booking

events_list = []
bookings_list = []

def validate_positive_integer(func):
    def wrapper(*args, **kwargs):
        try:
            val = func(*args, **kwargs)
            if int(val) <= 0:
                print("Error: Quantity must be positive.")
                return None
            return int(val)
        except ValueError:
            print("Error: Please enter a valid number.")
            return None
    return wrapper

calculate_price = lambda price, qty: price * qty

def load_data():
    global events_list, bookings_list

    if os.path.exists('events.csv'):
        with open('events.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                e = Event(row['event_id'], row['name'], row['total_tickets'], row['price'])
                e.available_tickets = int(row['available_tickets'])
                events_list.append(e)

    if os.path.exists('bookings.csv'):
        with open('bookings.csv', 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                b = Booking(row['event_id'], row['customer_name'], row['tickets_booked'])
                b.booking_id = row['booking_id']
                bookings_list.append(b)

    print("Data loaded successfully.")

def save_data():
    with open('events.csv', 'w', newline='') as f:
        writer = csv.DictWriter(
            f,
            fieldnames=['event_id', 'name', 'total_tickets', 'available_tickets', 'price']
        )
        writer.writeheader()
        for e in events_list:
            writer.writerow(e.to_dict())

    with open('bookings.csv', 'w', newline='') as f:
        writer = csv.DictWriter(
            f,
            fieldnames=['booking_id', 'event_id', 'customer_name', 'tickets_booked']
        )
        writer.writeheader()
        for b in bookings_list:
            writer.writerow(b.to_dict())

    print("Data saved. Exiting...")

def add_event():
    eid = input("Enter Event ID: ")
    name = input("Enter Event Name: ")
    total = input("Enter Total Tickets: ")
    price = input("Enter Ticket Price: ")

    new_event = Event(eid, name, total, price)
    events_list.append(new_event)
    print(f"Event '{name}' added successfully.")

@validate_positive_integer
def get_ticket_qty():
    return input("Enter number of tickets: ")

def book_ticket():
    print("\n--- Available Events ---")
    for e in events_list:
        print(e)

    eid = input("Enter Event ID to book: ")
    event = next((e for e in events_list if e.event_id == eid), None)

    if not event:
        print("Event not found!")
        return

    qty = get_ticket_qty()
    if not qty:
        return

    if qty > event.available_tickets:
        print(f"Error: Only {event.available_tickets} tickets available.")
        return

    name = input("Enter Customer Name: ")

    new_booking = Booking(eid, name, qty)
    bookings_list.append(new_booking)

    event.update_availability(qty, 'book')

    total_cost = calculate_price(event.price, qty)
    print(f"Booking Successful! ID: {new_booking.booking_id}. Total Cost: ${total_cost}")

def cancel_booking():
    bid = input("Enter Booking ID to cancel: ")
    booking = next((b for b in bookings_list if b.booking_id == bid), None)

    if not booking:
        print("Booking ID not found.")
        return

    event = next((e for e in events_list if e.event_id == booking.event_id), None)
    if event:
        event.update_availability(booking.tickets_booked, 'cancel')

    bookings_list.remove(booking)
    print(f"Booking {bid} cancelled successfully.")

def view_status():
    if not bookings_list:
        print("No bookings to display.")
        return

    data = [b.to_dict() for b in bookings_list]
    df = pd.DataFrame(data)
    print("\n--- Booking Summary (Pandas) ---")
    print(df)

def visualize_trends():
    if not bookings_list:
        print("Not enough data to visualize.")
        return

    event_counts = {}
    for b in bookings_list:
        event_counts[b.event_id] = event_counts.get(b.event_id, 0) + b.tickets_booked

    events = list(event_counts.keys())
    counts = list(event_counts.values())

    plt.bar(events, counts)
    plt.xlabel('Event ID')
    plt.ylabel('Tickets Sold')
    plt.title('Booking Trends per Event')
    plt.show()

def main():
    load_data()
    while True:
        print("\n=== Event Ticket Booking Tracker ===")
        print("1. Add Event")
        print("2. Book Ticket")
        print("3. Cancel Booking")
        print("4. View Status (Pandas)")
        print("5. Visualize Trends (Matplotlib)")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            add_event()
        elif choice == '2':
            book_ticket()
        elif choice == '3':
            cancel_booking()
        elif choice == '4':
            view_status()
        elif choice == '5':
            visualize_trends()
        elif choice == '6':
            save_data()
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()