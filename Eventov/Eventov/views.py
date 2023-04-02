from django.shortcuts import render

def loginOrSignup(request):
    return render(request, "index.html")