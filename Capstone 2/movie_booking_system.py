"""
Movie Booking System

Features:
1.	User Registration and Login:
    o	Users can register and log in to book tickets.
    o	Credentials are stored securely in memory.
2.	Movie and Show Management:
    o	Admin can add movies and show timings.
    o	Users can view available movies and their timings.
3.	Seat Booking:
    o	Users can select a movie, showtime, and book seats.
    o	Seats are dynamically updated based on availability.
4.	Booking History:
    o	Users can view their past bookings.
"""


class User:
    """
    User: 
        Handles user details, login, and registration
    """
    users = {}
    def __init__(self, name, username, password): # add setter method to set the ahshed password
        self.name = name
        self.username = username
        self.password = hash(password)
        self.bookings = [] # stores users booking history

    @classmethod
    def register(cls):
        name = input("Enter the name: ")
        username = input("Enter the username: ")
        if username in cls.users:
            print("Username already exists!!")
            return None
        password = input("Enter the password: ")
        """
        users = {
        "nainish": <User object: name, password,...>
        }
        """
        cls.users[username] = User(name, username, password)
        print("Registration Successfull!!")
        return cls.users[username]

    @classmethod
    def login(cls):
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        if username in cls.users and cls.users.get(username).password == hash(password):
            print("Login Successfull!!")
            return cls.users[username]
        print("Username or Password isn't correct!!")
        return None


class Movie:
    """
    Movie: 
        Stores information about movies, showtimes, and available seats.
    """
    def __init__(self, title, showtime, total_seats): # create getters and seteers methods for appropriate attributes
        self.title = title
        self.showtime = showtime
        self.total_seats = int(total_seats)
        self.available_seats = int(total_seats)
    
    def display_details(self):
        print(f"Movie: {self.title} | ShowTime: {self.showtime} | Seats Available: {self.available_seats}")


class Booking:
    """
    Booking:
       Manages booking information, such as movie, user, and seat details.
    """
    def __init__(self, user, movie, seats_booked): # create getters and setters for seat_booked obj attribute
        self.user = user
        self.movie = movie
        self.seats_booked = int(seats_booked)

    def display_details(self):
        print(f"User: {self.user.name} | Movie: {self.movie.title} | Showtime: {self.movie.showtime} | "
              f"Seats Booked: {self.seats_booked}")


class Admin:
    """
    Admin: 
        Manages movie and showtime additions.
    """
    movies = []
    def __init__(self, password):
        self.password = hash(password) # make a getter obj method for getting the password and setter obj method to set the password
    
    def get_password(self):
        pass

    def set_password(self, password):
        pass

    @classmethod
    def get_movies(cls):
        return cls.movies

    @classmethod
    def add_movie(cls):
        title = input("Enter the movie title: ")
        showtime = input("Enter the movie showtime: ")
        total_seats = input("Enter the total number of seats: ")
        cls.movies.append(Movie(title=title, showtime=showtime, total_seats=total_seats))
        print("Movie has been added successfully!!")


def main():
    admin = Admin(password=input("Enter the admin password: "))

    print("!!Movie Booking System!!")
    while True:
        try:
            print("\n1. Register\n2. Login\n3. Admin login\n4. Logout")
            choice = int(input("Enter you Choice: "))

            if choice == 1:
                User.register()
            elif choice == 2:
                user = User.login()
                if user:
                    print("Booking Menu!!")
                    while True:
                        print(f"\n1. View Movies\n2. Book Movie\n3. View Booking\n4. Logout")
                        user_choice = int(input("Enter your choice: "))
                        if user_choice == 1:
                            if admin.get_movies():
                                for movie in admin.get_movies():
                                    movie.display_details()
                            else:
                                print("No Movies to show!! please comeback later!!")
                        elif user_choice == 2:
                            if not admin.get_movies():
                                print("No Movies available!! Please comeback and book later!!")
                                continue
                            movie_title = input("Enter the Movie Title: ")
                            for movie in admin.get_movies():
                                if movie.title == movie_title:
                                    if movie.available_seats > 0:
                                        print(f"Available Seats: {movie.available_seats}")
                                        seat_to_book = int(input("Enter the number of seats: "))
                                        if movie.available_seats >= seat_to_book:
                                            movie.available_seats -= seat_to_book
                                            booking = Booking(user, movie, seat_to_book)
                                            user.bookings.append(booking)
                                            print("Booking Successfull!!")
                                        else:
                                            print("Not enough seats!!")
                                    else:
                                        print("Housefull!!")
                                else:
                                    print("Movie not found!!")
                        elif user_choice == 3:
                            if user.bookings:
                                for booking in user.bookings:
                                    booking.display_details()
                            else:
                                print("Time to book you first movie!!")
                        elif user_choice == 4:
                            print("Logging out!!!")
                            break
                        else:
                            print("Invalid input enter again!!")
            elif choice == 3:
                admin_password = input("Enter the admin password: ")
                if hash(admin_password) == admin.password:
                    print("Welcome To Admin Dashboard!!")
                    while True:
                        print("\n1. Add Movie\n2. View Movie\n3. Logout")
                        admin_choice = int(input("Enter the choice: "))
                        if admin_choice == 1:
                            admin.add_movie()
                        elif admin_choice == 2:
                            if admin.get_movies():
                                for movie in admin.get_movies():
                                    movie.display_details()
                            else:
                                print("Please add new movies!!")
                        elif admin_choice == 3:
                            print("Sayonaraa admin!!")
                            break
                        else:
                            print("Invalid Input!!")
                            break
            elif choice == 4:
                print("Thanks for using the movie booking system!!")
                break
            else:
                print("You have enter the wrong choice please enter again!!")
        except TypeError as e:
            print("Please Enter your choice as integer!!")



main()