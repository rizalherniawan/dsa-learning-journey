import logging

class AccessControl:
    roles = ["admin","user"]

    def __init__(self):
        self.authorized_users = set()
        self.role = None

    def add_user(self, user, role):
        self.authorized_users.add(user)
        if role in AccessControl.roles:
            self.role = role

    def remove_user(self, user):
        self.authorized_users.discard(user)

 
    
    def access_system(self, user):
        role = AccessControl.roles[AccessControl.roles.index(self.role)]
        is_user = user in self.authorized_users

        logging.getLogger().setLevel(logging.INFO)

        if role != None and is_user == True:
            logging.info(f"{user} with {role} successfully accessed system")
        else:
            logging.info(f"{user} as guest successfully accessed system")

        
    

# Contoh penggunaan
access_control = AccessControl()
access_control.add_user("Alice","admin")
print(access_control.check_access("Alice")) # Harusnya True
print(access_control.check_access("Bob")) # Harusnya False
access_control.access_system("Alice")
access_control.access_system("Bob")
