from django.shortcuts import render
from django.shortcuts import render_to_response
import json
from django.http import HttpResponse
from pnm.models import Paper,Note

# https://www.cnblogs.com/dasydong/p/4427806.html
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def home(request):
	return render_to_response('pnm.html',{})

def view(request,paper_id):
	paper=Paper.objects.get(id=paper_id)
	notes=paper.all_note()
	contents={'paper':paper,'notes':notes}
	return render_to_response('view.html',contents)

@csrf_exempt 
def add_note(request):
	paper_id=request.POST.get("paper_id")
	if paper_id:
		note_id=Note.create(paper_id).id
		return HttpResponse(note_id)
	return HttpResponse(-1)

@csrf_exempt 
def modify_note(request):
	note_id=request.POST.get("note_id")
	content=request.POST.get("content")
	if note_id:
		flag=Note.modify(note_id,content)
		return HttpResponse(flag)
	return HttpResponse(-1)

@csrf_exempt 
def delete_note(request):
	note_id=request.POST.get("note_id")
	if note_id:
		flag=Note.delete_note(note_id)
		return HttpResponse(flag)
	return HttpResponse(-1)
