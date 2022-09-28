import db_handler


def main():
    useresponse: str = input("1. Create account\n"
                             "2. Login\n\n"
                             "0. Cancel\n\n")
    if useresponse == '1':
        print("         ""Create account -\n")
        creat_user()
        response = input("\n\n0 to go back\n\n")
        if response == '0':
            print("          ""Welcome To This Twitter!!\n")
            main()
    elif useresponse == '2':
        print("         ""Login -\n")
        login()
        response = input("\n\n0 to go back\n\n")
        if response == '0':
            main()


def creat_user():
    full_name = input("Enter your Surname and Lastname: ")
    username = input("Enter your username: ")
    password = input("Enter your secure password: ")

    user = dict(fullName=full_name, name=username, password=password)

    old_db: list = db_handler.read_db()
    old_db.append(user)

    db_handler.write_to_db(old_db)


def login():
    username = input("Enter your username: ")
    password = input("Enter your secure password: ")

    db = db_handler.read_db()
    for user in db:
        if user["name"] == username and user["password"] == password:
            print(username + " Successfully logged in")
            print("""
                    WELCOME TO YOUR PROFILE -
                    
            Username - + user["name"]
            full name - + user["fullName"]
            
            status - The way up is the way down.
            
            Tweets & replies   Followers   Following   Media   Links
            
            
            
            1. Edit Profile
            2. Logout
            
            0. Cancel
            
            """)
        else:
            continue


def edit_profile():
    ...
