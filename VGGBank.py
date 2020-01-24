print('''
        Welcome to VGG Bank
        Press 1: create account
        Press 2: transaction
''')

customers_details = {}
balance = 0.0
def create_account():
    # Prompting the user to create an account.
    while True:
        users_choice = int(input('Please select 1 or 2 to do transaction: '))
        if users_choice == 1:
            email = input('Enter your email address: ')
            password = input('Enter a password: ')
            if email not in customers_details.keys():
                print('Account created successfully')


create_account()
