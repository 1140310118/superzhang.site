from django.db import models
from django.contrib import admin

# Create your models here.
class Catalog(models.Model):
	name = models.CharField(max_length=150)
	parent = models.ForeignKey('Catalog',null=True,blank=True)
	
	def __str__(self):
		return str(self.id)+"、"+self.name

class Paper(models.Model):
	name = models.CharField(max_length=150)
	catalog = models.ForeignKey('Catalog')
	# 0 pdf; 1 website.
	paper_type = models.CharField(max_length = 2)
	url = models.CharField(max_length=150, default="")

	def __str__(self):
		return str(self.id)+"、"+self.name

	def all_note(self):
		return Note.objects.filter(paper_id=self.id)

class Note(models.Model):
	paper=models.ForeignKey('Paper')
	content=models.TextField(null=True,blank=True)

	def __str__(self):
		return str(self.id)+str(self.paper_id)

	@classmethod
	def create(cls,paper_id):
		note = cls(paper_id=paper_id)
		note.save()
		return note

	@classmethod
	def modify(cls,note_id,content):
		try:
			note=cls.objects.get(id=note_id)
			note.content=content
			note.save()
			return 1
		except:
			return -1

	@classmethod
	def delete_note(cls,note_id):
		try:
			cls.objects.get(id=note_id).delete()
			return 1
		except:
			return -1


class CatalogAdmin(admin.ModelAdmin):
    list_display = ('id','name','parent')

class PaperAdmin(admin.ModelAdmin):
    list_display = ('id','name','catalog','paper_type','url')

class NoteAdmin(admin.ModelAdmin):
    list_display = ('id','paper','content')

admin.site.register(Catalog,CatalogAdmin)
admin.site.register(Paper,PaperAdmin)
admin.site.register(Note,NoteAdmin)