from django.shortcuts import render, redirect,get_object_or_404
from .models import Post



def	post_list(request):
	posts = Post.objects.all().order_by('-created_at')

	return	render(request,	'blog\post_list.html',	{'posts':	posts})
def details_posts(request,id):
	post=get_object_or_404(Post,id=id)
	print("#===*40")
	print(post)
	print("#===*40")
	return render(request,'blog\posts_détail.html',{'post':post})

def home(request):
     return render(request, 'blog/index.html')
    

def blog(request):
	posts = Post.objects.all().order_by('-created_at')

	return	render(request,	'blog\post_list.html',	{'posts':	posts})

# Create your views here.