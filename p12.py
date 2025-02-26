l=[]

def signup():
    print("Create a new account.")
    email = input("Enter the email: ")
    password = input("Enter the password: ")
    
    for user in l:
        if user["email"] == email:
            print("Account already exists. You need to sign in.")
    a = {"email": email, "password":  password}
    l.append(a)
    print(l)
    print("Account created successfully.")
    
def signin():   
    email = input("Enter the email: ")
    password = input("Enter the password: ")
    
    for user in l:
        if user["email"]==email and user["password"]==password:
            print("Signed in successfully")
    print("Invalid details")

def main():
    while True:  
        print("1. Sign Up")
        print("2. Sign In")
        print("3. Exit")
        
        c = input("Enter your choice: ")
        
        if c == "1":
            signup()
        elif c == "2":
            signin()
        elif c == "3":
            print("Exit")
            break
        else:
            print("Invalid choice.")
main()
    