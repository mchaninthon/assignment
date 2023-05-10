import json
import datetime
from movie import Movie
from users import User
from bookings import Booking

print("Welcome to Cinemax. Here is what you can do today.")
print("Use the menu options below to navigate the program:")

while True:
    print("\nMenu Options:")
    print("1. Display movies")
    print("2. Book a ticket")
    print("3. Show ticket list")
    print("4. Get movie details")
    print("5. Exit program")

    choice = input("Enter your choice (1-5): ")

    if choice == '1':
        movies = Movie(1)
        movies.display_movies()

    elif choice == '2':
        booking = Booking(1)
        booking.book_ticket()

    elif choice == '3':
        booking = Booking()
        booking.show_bookings()

    elif choice == '4':
        movie_id = int(input("Enter movie id: "))
        with open('cinema_data.json') as f:
            data = json.load(f)
        if str(movie_id) in data['movies']:
            movie_data = data['movies'][str(movie_id)]
            print(f"Title: {movie_data['title']}")
            print(f"Genre: {movie_data['genre']}")
            print(f"Duration: {movie_data['duration']} min")
            print(f"Synopsis: {movie_data['synopsis']}")
        else:
            print("Invalid movie id")

    elif choice == '5':
        print("Goodbye!")
        exit()

    else:
        print("Invalid choice. Please enter a number between 1 and 5.")




   





