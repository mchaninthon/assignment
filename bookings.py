import json
import datetime
from users import User      
# Load cinema data from file
with open('cinema_data.json', 'r') as f:
    cinema_data = json.load(f)

class Booking:
    def __init__(self, booking_id):
        self.booking_id = booking_id
        # self.customer_name = customer_name
        # self.show_time = show_time
        # self.movie_id = movie_id
        
    # Define a function to book a ticket
    # Define a function to book a ticket
    def book_ticket():
        user = User() # Create a User instance
        user_id = user.user_id

        # Get user input for movie and showtime
        name = input("Enter your name")
        movie_id = int(input("Enter movie ID: "))
        showtime = input("Enter showtime (HH:MM): ")
        num_tickets = int(input("Enter number of tickets: "))

        # Find the movie in the cinema data
        movie = None
        for m in cinema_data['movies']:
            if m['id'] == movie_id:
                movie = m
                break
        if not movie:
            print("Invalid movie ID.")
            return
        
        # Check if theater is full or the booking is still ongoing
        count = 0
        available_seats = cinema_data['theater']['seats']
        for booking in cinema_data['bookings']:
            if booking['movie_id'] == movie_id and booking['showtime'] == showtime:
                count += booking['num_tickets']
        if count >= available_seats:
            print("Tickets are sold out")
            return

        # Add booking to transaction file
        with open('bookings.json', 'a') as f:
            booking_id = len(cinema_data['bookings']) + 1
            customer_name = name
            date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            booking = {"id": booking_id, "name": customer_name, "datetime": date_time,
                    "movie_id": movie_id, "showtime": showtime, "num_tickets": num_tickets}
            cinema_data['bookings'].append(booking)
            json.dump(booking, f)
            f.write('\n')

        # Save user instance as well to the cinema_data JSON file
        cinema_data['user'] = {
            "user_id": user_id,
            "username": name,
            "bookings": [booking_id]
        }

        print(f"{num_tickets} ticket(s) for {movie['title']} at {showtime} on {date_time} "
            f"have been booked for {customer_name}. Enjoy the movie!")

        # Update cinema_data JSON file
        with open('cinema_data.json', 'w') as f:
            json.dump(cinema_data, f)


    
    # Define a method to show all bookings starting with the most recent
    def show_bookings(self):
        bookings = cinema_data['bookings']
        bookings.reverse()  # Reverse the list so that the most recent booking is displayed first
        for booking in bookings:
            print(f"Booking ID: {booking['id']}")
            print(f"Customer Name: {booking['name']}")
            print(f"Movie ID: {booking['movie_id']}")
            print(f"Showtime: {booking['showtime']}")
            print(f"Number of Tickets: {booking['num_tickets']}")
            print(f"Booking Date and Time: {booking['datetime']}")
            print("---------------")





