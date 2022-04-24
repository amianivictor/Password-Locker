import random
from user import user


def main():
    while True:
        print('welcome to password locker app!')
        print('n')
        print("chose a code to navigate through the app: new user use 'nu':logging in use 'lg':to exit use 'ex'")
        short_code = input().lower()
        print('\n')

        if short_code == 'nu':
            print('create username')
            created_user_name = input()


            

