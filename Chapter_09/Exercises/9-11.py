from admin import *

# 在其中创建一个Admin 实例
# 并对其调用方法show_privileges() ，以确认一切都能正确地运行。

admin_privileges = Privileges()

admin_user = Admin('Jack','Liu',admin_privileges,gender = 'age', age = 21)
admin_user.privileges.show_privileges(admin_user.first_name)