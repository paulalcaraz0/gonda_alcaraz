game_library = {
    "Donkey Kong" : { "quantity" :  3, "cost" : 2},
    "Super Mario Bros" : { "quantity" : 5, "cost" : 3},
    "Tetris" : {"quantity " : 2,"cost " : 1}
}

user_database = {}

inventory = []

admin_name = "admin"
admin_pass = "adminpass"

def display_games():
    print(game_library)

def rent_game(username):
    print(f"Available games for rent. Your current balance: ${user_database[username]['money']}:")
    for i, (game, details) in enumerate(game_library.items(), start=1):
        print(f"{i}. {game} - Quantity: {details['quantity']}, Cost: ${details['cost']}")
    choice = int(input("Enter the number of the game you want to rent: "))
    if choice in range(1, len(game_library) + 1):
        game_name = list(game_library.keys())[choice - 1]
        quantity = int(input("How many copies?: "))
        if game_library[game_name]["quantity"] >= quantity:
            total_cost = game_library[game_name]["cost"] * quantity
            if user_database[username]['money'] >= total_cost: 
                user_database[username]['money'] -= total_cost  
                inventory.append({"game_name": game_name, "quantity": quantity, "username": username})
                game_library[game_name]["quantity"] -= quantity
                print(f"Total Cost: ${total_cost}")
            else:
                print("Insufficient funds.")
        else:
            print("Insufficient quantity.")
    else:
        print("Enter a valid input.")

def topup(username, money):
    add_money = float(input("Input the amount you want to add"))
    current_money= user_database[username]['money'] + add_money

    print(f"Current money is {current_money}")
    choice = input(" Continue? Y/N")

def display():
    print(inventory)
    pass

def redeem():
    pass

def checkpts():
    pass


def logged_inmenu(username):
    while True:
        print(f'Logged in as {username}')
        print(f'current balance: ${user_database[username]["money"]}')
        print(""" WELCOME TO GAME RENTAL SYSTEM
              1. Rent a Game
              2. Return Game
              3. Top_up account
              4. Display Inventory
              5.Redeem Free Game rental
              6. Check Points
              7. Logout""")
        choice = int(input("Choose your coice"))
        if choice == 1:
            rent_game(username)
        elif choice == 2:
            pass
        elif choice == 3:
            pass
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        elif choice == 6:
            pass
        elif choice == 7:
            main()
    

def register():
    username = input("REGISTER USER\n\n INPUT YOUR USERNAME")
    password = input("Input passwird: ")

    user_database [username] = {
        'username' : username,
        'password' : password,
        'money' : 0 
    }
    if not username:
        main()
    if username in user_database[username]:
        print("Username is already exists")
        register()
    if len(password) >= 8:
        print("sign up successful")
        main()
    else:
        print("Invalid input")
        register()

def login():
    print("USER LOGIN\n\n")
    username = input("IInput your username")
    if not username:
        main()
    password = input("Input password")
    if user_database .get(username) and user_database[username]['password'] == password:
        print("Sign Successfully")
        logged_inmenu(username)

def admin_login():
    adminuser = input("Input admin username")
    adminpass = input("Input admin password")

    if adminuser == admin_name and adminpass == admin_pass:
        admin_menu()
    else:
        print("INCORRECT try again")
        admin_login()

def edit_game():
    pass

def admin_menu():
    print("Welcome to admin menu\n\n 1. Edit Game Details\n 2. Logout")
    choice = int(input("Input choice"))
    if choice == 1:
        edit_game()
    elif choice == 2:
        main()







def main():
    print("""MAIN MENU
          1. Display Available Games
          2. Register User
          3. Sign In
          4. Admin Sign In
          5. Exit Program""")
    while True:
        choice = int(input("ENTER YOUR CHOICE"))
        try:
            if choice == 1:
                display_games()
            elif choice == 2:
                register()
            elif choice == 3:
                login()
            elif choice == 4:
                admin_login()
            elif choice == 5:
                exit()
        except ValueError:
            pass
main()