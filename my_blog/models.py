from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField

class Message(models.Model):
	name=models.CharField(max_length=36)
	email=models.EmailField(blank=True)
	phone=models.CharField(max_length=21)
	message=models.CharField(max_length=300)
	created=models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return "Name: "+self.name


class PostType(models.Model):
	title=models.CharField(max_length=60)
	def __str__(self):
		return self.title

class Blog(models.Model):
	title=models.CharField(max_length=120)
	description=models.CharField(max_length=120)
	date=models.DateField()
	new_content=RichTextUploadingField()
	post_type=models.ForeignKey('my_blog.PostType',on_delete=models.DO_NOTHING,blank=True)
	def __str__(self):
		return "Blog "+str(self.id)+": "+self.title


# Create your models here.
