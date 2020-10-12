import datetime as dt

def time_registered():
    register = dt.date.today()
    regdetail = print(f"You joined this platform on: {register}")
    return regdetail
detailserror = "the details you entered are incorrect, please try again"
welcomenote = print("\n\nHello there!! lets create you a new profile\n")
username_create = input("Hello dear, please type in a NEW USERNAME: ")
username = username_create
pin_creation = input(f"Welcome {username}, please type in NEW PASSWORD: ")
pin = pin_creation
print(f"\nThanks for registering. Now login your details below\n\n")
while True:
    usernamelog = input("username: ")
    passwordlog = input("password: ")
    if usernamelog == username and passwordlog == pin:
        break
    else:
        print(f"\n{detailserror}\n")
        usernamelog
        passwordlog
print(f"Hello!\n{time_registered()}\nWe are so glad you joined our company,\nwe will make life wonderful for you!")