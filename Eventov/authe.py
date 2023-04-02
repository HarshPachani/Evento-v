import pyrebase
firebaseConfig = {
    "apiKey": "AIzaSyBJaxw5gaWuIudkXhXl5BNQmsYgJ1CclEU",
    "authDomain": "evento-v-912ee.firebaseapp.com",
    "databaseURL": "https://evento-v-912ee-default-rtdb.firebaseio.com",
    "projectId": "evento-v-912ee",
    "storageBucket": "evento-v-912ee.appspot.com",
    "messagingSenderId": "778926219586",
    "appId": "1:778926219586:web:537e33c28d64ee858f28db",
    "measurementId": "G-C3DLBVYQXW"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

def signUp():
    email = input("Enter email")
    password = input("Enter password")
    try:
        auth.create_user_with_email_and_password(email, password)
    except Exception as e:
        print(f"Email already Exist: {e}")

def signIn():
    email = input("Enter email")
    password = input("Enter password")
    try:
        auth.sign_in_with_email_and_password(email, password)
    except:
        print("Invalid email or pass")

signUp()
signIn()