from  django.urls	import	path
from .views	import	post_list, details_posts

urlpatterns	=	[
	path('',post_list,	name='post_list'),
	path('<int:id>', details_posts,name='details_posts')
]