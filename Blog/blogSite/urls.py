from django.urls import path

from blogSite import views
from . import views

urlpatterns = [
    path('',views.FirstPage,name='firstPage'),
    path('posts',views.AllPost,name='All-Posts'),
    path('posts/<slug:slug>',views.PostDetails,name='Post-Details'),
    path('read-later',views.readLater,name='read-later')
]