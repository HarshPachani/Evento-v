from django.shortcuts import render
from django.http import HttpResponse
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

def loginOrSignup(request):
    return render(request, "index.html")

def signedUp(request):
    fullName = request.POST.get("name")
    mobile = request.POST.get("mobile")
    email = request.POST.get("email")
    password = request.POST.get("password")
    confirmPassword = request.POST.get("confirmPassword")

    if password == confirmPassword:
        try:
            auth.create_user_with_email_and_password(email, password)
        except:
            message = "Account Already Exists"
            return render(request, "signedUp.html", {"message": message})            
    else:
        message = "Password and confirm password doesn't match"
        return render(request, "signedUp.html", {"message": message})
    
    message = "Account Created Successfully!"
    return render(request, "signedUp.html", {"message": message})

def signedIn(request):
    email = request.POST.get("email")
    password = request.POST.get("password")

    try:
        auth.sign_in_with_email_and_password(email, password)
    except:
        message = "Invalid Credentials"
        return render(request, "signedIn.html", {"message": message})
    
    message = "Welcome to Evento-v!"
    return render(request, "signedIn.html", {"message": message})