class User:
    def __init__(self, name):
        self.name = name
        print("Creating name.. ")

user_1 = User("dan")
print(user_1.name)