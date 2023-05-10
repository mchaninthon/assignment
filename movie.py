import json

# Load cinema data from file
with open('cinema_data.json', 'r') as f:
    cinema_data = json.load(f)

class Movie:
    def __init__(self, movie_id):
        self.movie_id = movie_id
        # self.title = title
        # self.price = price
        # self.release_date = release_date
        # self.show_times = show_times

        # Define a function to display available movies and show times

    # Define a function to display available movies and show times
    def display_movies(self):
        print("Today's movies:")
        for movie in cinema_data['movies']:
            print(f"{movie['title']} (ID: {movie['id']})")
            for showtime in movie['showtimes']:
                print(f" - {showtime}")

    def get_movie_info(self, movie_id):
        for movie in cinema_data['movies']:
            if movie['id'] == movie_id:
                return f"{movie['title']} (ID: {movie['id']})\nPrice: {movie['price']}\nRelease Date: {movie['release_date']}\nShow Times: {movie['showtimes']}"

        