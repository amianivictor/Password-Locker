#!/usr/bin/env python3.8
from user import User
from user import Credentials


def create_user(username,password):
    '''
    Function to create a new user
    '''
    new_user = User(username,password)
    return new_user

def save_user(user):
    '''
    Function to save user
    '''
    user.save_user()

def delete_user(user):
    '''
    Function to delete a user
    '''
    user.delete_user()

def display_user():
    """
    Function to display existing user
    """
    return User.display_user()
# ................................. User  ....................................


def verify_user(username,password):
	'''
	Function that verifies the existance of the user before creating credentials
	'''
	checking_user = Credentials.verify_user(username,password)
	return checking_user

def generate_password():
    '''
	Function to generate a password automatically
	'''
    gen_password = Credentials.generatePassword()
    return gen_password

def copy_password(account_name):
    """
    A function that copies the password using the pyperclip framework
    We import the framework then declare a function that copies the emails.
    """
    return Credentials.copy_password(account_name)


# .................................Credentials......................................

def create_new_credentials(account_name,username,password):
    '''
	Function to create a new credential
	'''
    new_credentials = Credentials(account_name,username,password)
    return new_credentials

def save_credentials(credentials):
    """
    Function to save Credentials to the credentials list
    """
    credentials.save_credentials()

def find_credentials(account_name):
    return Credentials.find_credentials(account_name)

def check_existing_credentials(account_name):
    return Credentials.credentials_exist(account_name)


def delete_credentials(credentials):
    """
    Function to delete a Credentials from credentials list
    """
    credentials.delete_credentials()

def display_credentials():  
    """
    Function that returns all the saved credential.
    """
    return Credentials.display_credentials()

# ............................................main..............

def main():
	print(' ')
	print('Hello! Welcome to smart password.')
	while True:
		print(' ')
		print("-"*60)
		print('Use these codes to navigate: \n ca-Create an Account \n li-Log In \n ex-Exit')
		short_code = input('Enter a choice: ').lower().strip()
		if short_code == 'ex':
			break

		elif short_code == 'ca':
			print("-"*60)
			print(' ')
			print('To create a new account:')
			username = input('Enter your username : ').strip()
			password = input('Enter your password : ').strip()
			save_user(create_user(username,password))
			print(" ")
			print(f' Account Created for: {username}  using password: {password}')
		elif short_code == 'li':
			print("-"*60)
			print(' ')
			print('To login, enter your account credentials:')
			user_name = input('Enter your username : ').strip()
			password = str(input('Enter your password : '))
			user_exists = verify_user(username,password)
			if user_exists == username:
				print(" ")
				print(f'Welcome {username}. Please choose an option to continue.')
				print(' ')
				while True:
					print("-"*60)
					print('Navigate using the following codes: \n cc-Create a Credential \n dc-Display Credentials \n copy-Copy Password \n ex-Exit')
					short_code = input('Enter a code: ').lower().strip()
					print("-"*60)
					if short_code == 'ex':
						print(" ")
						print(f'Goodbye {username}')
						break
					elif short_code == 'cc':
						print(' ')
						print('Enter your credential details:')
						account_name = input('Enter the account name: ').strip()
						username = input('Enter your account username - ').strip()
						while True:
							print(' ')
							print("-"*60)
							print('Please choose an option for entering a password: \n ep-enter existing password \n gp-generate a password \n ex-exit')
							password_choice = input('Enter an option: ').lower().strip()
							print("-"*60)
							if password_choice == 'ep':
								print(" ")
								password = input('Enter your password: ').strip()
								break
							elif password_choice == 'gp':
								password = generate_password()
								break
							elif password_choice == 'ex':
								break
							else:
								print('You have entered the wrong option. Try again.')
						save_credentials(create_new_credentials(account_name,username,password))
						print(' ')
						print(f'Credentials Created: Account Name: {account_name} , Username {username}, Password: {password}')
						print(' ')
					elif short_code == 'dc':
						print(' ')
						if display_credentials():
							print('Here is a list of all your credentials')
							print(' ')
							for credential in display_credentials():
								print(f' Account Name: {credential.account_name}, Username {credential.username} , Password: {credential.password}')
							print(' ')	
						else:
							print(' ')
							print("You don't seem to have any credentials saved yet")
							print(' ')
					elif short_code == 'copy':
						print(' ')
						chosen_site = input('Enter the account name for the credential password to copy: ')
						copy_password(chosen_site)
						print('')
					else:
						print('Oops! Wrong option entered. Try again.')

			else: 
				print(' ')
				print('You have enetered the wrong credentials. Try again .')		
		
		else:
			print("-"*60)
			print(' ')
			print('Wrong option. Try again.')
				





 
if __name__ == '__main__':
    main()

    
