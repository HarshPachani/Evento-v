from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def postsignin(request):
    email = request.POST.get('email')
    password = request.POST.get('password')
    if email == "harshpachani@gmail.com" and password == "123456":
        message = f"welcome {email}"
        return render(request, 'index.html', {"message": message})
    else:
        message = "Invalid email or password"
        return render(request, 'index.html', {"message": message})