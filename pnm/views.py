from django.shortcuts import render,render_to_response

# Create your views here.

def home(request):
	return render_to_response('pnm.html',{})

def view(request,url):
	return render_to_response('view.html',{})