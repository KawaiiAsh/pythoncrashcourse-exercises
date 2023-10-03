import privileges
import admin

web_admin_privileges = privileges.Privileges() 
web_admin = admin.Admin('Ash','Li',web_admin_privileges)
web_admin.privileges.show_privileges(web_admin.first_name)