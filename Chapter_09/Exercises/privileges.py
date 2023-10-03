class Privileges():
    def __init__(self):
        self.privileges = ["can add post","can delete post","can ban user"]

    def show_privileges(self,admin_instance):
        for privilege in self.privileges:
            print(admin_instance + " " + privilege)