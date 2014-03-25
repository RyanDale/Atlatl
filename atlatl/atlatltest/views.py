from django.shortcuts import render,  HttpResponse, HttpResponseRedirect
from atlatltest.models import House, Owner

def houses(request):
	return render(request, "atlatltest/houses.html",{
			"houses":House.objects.all(),
			"owners":Owner.objects.all(),
		})