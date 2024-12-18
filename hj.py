class User:
    def __init__(self, username, password):
        self.__username = username
        self.__password = password

    def set_password(self):
        if len(self.__password) < 8:
            return "Password must be 8 characters long."
        if not any(char.isdigit() for char in self.__password):
            return "Password must contain at least one digit."
        if not any(char in "!@#$%^&*()_+?" for char in self.__password):
            return "Password must contain at least one special character."
        if not self.__password[0].isupper():
            return "First character must be in upper case."
        return "Password is valid."

    def check_password(self):
        if self.set_password()=="Password is valid.":
            return "Password validation done!! it is crt"
        else:
            return "Password validation done!! it is  not crt"


# Create a User object
name=input("Enter your name: ")
password=input("Enter your password: ")

user = User(name,password)
print(user.set_password())
print(user.check_password())
