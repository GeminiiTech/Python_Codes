import json


def save_details(filePath,data):
    with open(filePath,"w") as f:
        json.dump(data,f)

def load_details(filePath):
    try:
        with open(filePath,"r") as f:
            data = json.load(f)
            return data
    except:
        return {}

def login(details):
    l_email = input('Enter Email:')
    if l_email.__contains__('@gmail.com'):
        if l_email in details:
            password = details[l_email]
            l_password = input("Enter your Password: ")
            if l_password == password:
                currentUser = l_email.split('@')
                currentUser2 = currentUser[0]
                currentUser3 = currentUser2[0].upper()
                currentUser4 = currentUser3 + currentUser2[1:]
                print("Logged in as " + currentUser4 )
        else:
            print("User Not Found")    
    else:
        print("Enter Valid Email")        

def register(details,filePath):
    r_email = input('Enter Email:')
    if r_email in details:
        print("User Already Exists")
        print("Login Now!")
        login(details)
    else:
        if r_email.endswith('@gmail.com'):
            pw1 = input("Enter your Password: ")
            pw2 = input("Confirm Password: ")
            if pw1 == pw2:
                r_password = pw1
                details[r_email] = r_password
                save_details(filePath,details)
                print("Account was created for " + r_email + " successfully")
            else:
                print("Passwords don't match....")    
        else:
            print("Enter a Valid Email")    

def IntroPage(details,filePath):
    print("Welcome!")
    print("1. Login")
    print("2. Register")
    action = int(input("What will you like to do?: "))
    if action == 1:
        login(details)
    elif action == 2:
        register(details,filePath)
    else:
        print("Wrong Input")        

# VARIABLES
# STORES THE JSON FILE
file_path = 'details.json'
# STORES THE CURRENT CONTENT OF THE JSON FILE
info  = load_details(file_path)    



IntroPage(info,file_path)