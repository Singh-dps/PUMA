# Event Ticket Booking System

A Python-based command-line application for managing event ticket bookings. This case study demonstrates object-oriented programming, data persistence with CSV, data analysis with pandas, and visualization with matplotlib.

## Features

- **Add Events**: Create new events with ID, name, total tickets, and price
- **Book Tickets**: Reserve tickets for customers with validation
- **Cancel Bookings**: Remove existing bookings and restore ticket availability
- **View Status**: Display booking summary using pandas DataFrame
- **Visualize Trends**: Generate bar charts showing ticket sales per event using matplotlib
- **Data Persistence**: Automatic saving and loading of events and bookings to/from CSV files

## Requirements

- Python 3.6+
- pandas
- matplotlib

## Installation

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd python-case-study
   ```

2. Create a virtual environment:
   ```bash
   python -m venv .venv
   ```

3. Activate the virtual environment:
   ```bash
   source .venv/bin/activate
   ```

4. Install dependencies:
   ```bash
   pip install pandas matplotlib
   ```

## Usage

Run the application:
```bash
python ticket_main.py
```

Follow the interactive menu to:
1. Add new events
2. Book tickets for available events
3. Cancel existing bookings
4. View booking status in tabular format
5. Visualize booking trends with charts
6. Exit (automatically saves data)

## Project Structure

- `ticket_main.py`: Main application logic and user interface
- `event_class.py`: Event class definition with ticket management
- `booking_class.py`: Booking class definition with unique ID generation
- `events.csv`: CSV file storing event data
- `bookings.csv`: CSV file storing booking data (created automatically)

## Data Files

The application uses CSV files for data persistence:
- Events are stored in `events.csv` with columns: event_id, name, total_tickets, available_tickets, price
- Bookings are stored in `bookings.csv` with columns: booking_id, event_id, customer_name, tickets_booked

## Example Usage

```
=== Event Ticket Booking Tracker ===
1. Add Event
2. Book Ticket
3. Cancel Booking
4. View Status (Pandas)
5. Visualize Trends (Matplotlib)
6. Exit

Enter choice: 1
Enter Event ID: 104
Enter Event Name: Jazz Night
Enter Total Tickets: 300
Enter Ticket Price: 25
Event 'Jazz Night' added successfully.
```

## Contributing

This is a case study project. Feel free to fork and modify for learning purposes.

## License

MIT License# PUMA
# gibberish-encrypter-decrypter
