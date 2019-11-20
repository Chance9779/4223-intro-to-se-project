# user class
# takes in static passcode for authentication
# sets boolean to tell if the user is an admin
class User():

    def __init__(self, pw):
        if (pw == '12345'):
            self.admin_bool = true
        else:
            self.admin_bool = false

    def get_admin(self):
        return self.admin_bool
