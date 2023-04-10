from django.shortcuts import render
def index(request):
    return render(request, 'index.html')

def submit(request):
    name = request.POST.get('text')
    if name == "Harsh":
        message = "Harsh"
        return render(request, 'index.html', {"message": message})
    else:
        return render(request, 'index.html')