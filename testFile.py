#import
from magti_fun import send_message

''' get user login info '''
with open("login_info.txt") as file:
    # get username and password
    user_= file.readline().strip()
    password_  = file.readline().strip()


''' single case '''  
##numbers_ = "591012340"
##messages_ = "Python is really cool!"

''' multi case '''
numbers_ = ["591012340"] * 40
messages_ = ["Python is really cool! _ {}".format(i + 1) for i in range(40)]



''' test '''
##send_message(username, password, numbers, messages, show_browser=False, close_after = True):
   
send_message(user_, password_, numbers_, messages_ , True, True)
