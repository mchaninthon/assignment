import random
#define class user its properties and methods
class User:
    def __init__(self, name):
        self.user_id = str(random.randint(10000, 99999))
        self.name = name
        self.bookings = []
    
    def get_user(self):
        return f"User ID: {self.user_id}, Name: {self.name}, Bookings: {self.bookings}"
    def save_user(self, user_id, name, bookings):
        user
        