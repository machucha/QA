class User:

    def __init__(self, first_name, last_name):
        self.username = first_name
        self.userlastname = last_name

    def say_first_name(self):
        print(self.username)

    def say_last_name(self):
        print(self.userlastname)

    def say_full(self):
        print("Моё имя", self.username, "и моя фамилия", self.userlastname)
