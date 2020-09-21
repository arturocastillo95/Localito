from django.shortcuts import render
from localito.custom_decorators import anonymous_required

# Create your views here.

@anonymous_required(redirect_url='dashboard')
def homeScreenView(request):
	context = {}
	return render(request, "pagemanager/home.html", context)