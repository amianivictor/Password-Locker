import random
from user import user


def main():
    while True:
        print('Hello welcome to password locker application!')
        print('n')
        print("You can chose the following commands to navigate the app: new user use 'nu':logging in use 'lg':to exit use 'ex'")
        short_code = input().lower()
        print('\n')

        if short_code == 'nu':
            print('create username')
            created_user_name = input()

            print('create password')
            created_user_password = input()

            print('confirm password')
            confirm_password = input()

            while confirm_password != created_user_password:
                print("invalid password did not match!!")
                print("enter your password")
                created_user_password = input()
                print("confrim your password")
                confirm_password = input()

            else:
                print(f"congratulations {created_user_name}! account creation successful")
                print('\n')
                print("continue to login")
                print("Username")
                entered_username =input()
                print("your password")
                entered_password =input()

            while entered_username != created_user_name or entered_password != created_user_password:
                print("Invalid username or password")
                print("Username")
                entered_username = input()
                print("your password")
                entered_password =input()

            else:
                print(f"welcome: {entered_username} to your account")
                print("\n")

        elif short_code == 'lg':
            print("welcome")
            print("enter user name")
            default_user_name = input()

            print("enter password")
            default_user_password = input()
            print("\n")

            while default_user_name != 'testuser' or default_user_password != '012345':
                print ("wrong userName or password. Username 'testuser' and password '012345' ")
                print("enter user name")
                default_user_name = input()

                print("enter password")
                default_user_password = input()
                print("\n")

            else:
                print("login success")
                print('\n')

        elif short_code == "ex":
            break
        else: 
            print("enter valid code to continue")

if __name__ == '__main__':
    main()                    


     











