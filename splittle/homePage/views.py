from django.shortcuts import render

def homePage(request):
    username = request.user.username
    return render(request, 'homePage.html', {'username':username})
