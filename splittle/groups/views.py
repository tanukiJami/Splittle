from django.shortcuts import render

def viewGroups(request):
    return render(request, 'viewGroups.html')

def createGroup(request):
    return render(request, 'createGroup.html')
