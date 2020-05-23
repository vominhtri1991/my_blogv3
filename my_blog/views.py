from django.shortcuts import render,get_object_or_404, redirect
from .models import Blog, PostType, Message
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import send_mail

#def myblog(request):
	#blogs=Blog.objects.order_by('-date')[:9]
	#return render(request,'my_blog/index.html',{'blogs':blogs})

def myblog(request):
	blogs=Blog.objects.order_by('-date')
	page = request.GET.get('page', 1)
	paginator = Paginator(blogs, 26)
	try:
		blogs = paginator.page(page)
	except PageNotAnInteger:
		blogs = paginator.page(1)
	except EmptyPage:
		blogs = paginator.page(paginator.num_pages)
	return render(request,'my_blog/index.html',{'blogs':blogs})

def about(request):
	return render(request,'my_blog/about.html')

def post(request,blog_id):
	blog=get_object_or_404(Blog,pk=blog_id)
	return render(request,'my_blog/post.html',{'blog':blog})

def contact(request):
	return render(request,'my_blog/contact.html')

def nav(request):
	return render(request,'my_blog/base_navg.html')	

def post_by_topic(request,id_type):
	topic=get_object_or_404(PostType,pk=id_type)
	posts=Blog.objects.filter(post_type=topic).order_by('-date')
	page = request.GET.get('page', 1)
	paginator = Paginator(posts, 3)
	try:
		posts = paginator.page(page)
	except PageNotAnInteger:
		posts = paginator.page(1)
	except EmptyPage:
		posts = paginator.page(paginator.num_pages)
	return render(request,'my_blog/post_by_topic.html',{'topic':topic,'posts':posts})	
# Create your views here.

def search(request):
	keyword=request.GET.get('keyword')
	posts=Blog.objects.filter(new_content__icontains=keyword)
	return render(request,'my_blog/result.html',{'key':keyword,'posts':posts})

def sendmail(request):
	if(request.method=='GET'):
		return render(request,'my_blog/contact.html')
	else:
		name=request.POST['name_sender']
		email=request.POST['email']
		message=request.POST['message']
		phone=request.POST['phone']
		if(name == "") or (email == "") or (message == ""):
			return render(request,'my_blog/contact.html',{'error':'Email, Name and Message cannot be empty.Please try again'})
		else:
			new_mes=Message.objects.create(name=name,email=email,phone=phone,message=message)
			new_mes.save()
			return redirect('myblog')