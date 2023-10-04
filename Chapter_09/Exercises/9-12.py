from privileges import Privileges
from admin import Admin

web_admin_privileges = Privileges() 
web_admin = Admin('Jack','Li',web_admin_privileges)
web_admin.privileges.show_privileges(web_admin.first_name)