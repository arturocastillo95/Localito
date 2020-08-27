from django.shortcuts import render

# Create your views here.

def homeScreenView(request):
	context = {}
	return render(request, "pagemanager/home.html", context)