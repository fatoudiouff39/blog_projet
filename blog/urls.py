from django .urls import path # type: ignore
from .views import post_list
from .views import details_posts , blog , home
urlpatterns = [
       path('Post/', post_list, name='post_list'),

       path('post/<int:id>',details_posts,name='post_detail'),

       path('vers_blog/',blog,name='blog'),

       path('index/',home,name='home'),
]