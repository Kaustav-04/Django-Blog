from django.shortcuts import render
from datetime import date
from .models import Post

# Create your views here.


def FirstPage(req):
    filteredPost = Post.objects.all().order_by('-date')[:3]
    return render(req,'blogSite/index.html',{
        'posts':filteredPost
    })

def AllPost(req):
    Posts = Post.objects.all().order_by('-date')
    return render(req,'blogSite/AllPost.html',{
        'Posts':Posts
    })

def PostDetails(req,slug):
    requiredPost = Post.objects.get(slug = slug)
    # for i in posts:
    #     if i['slug'] == slug:
    #         return render(req,'blogSite/PostDetail.html',{
    #             'postData': i
    #         })
    #     else:
    #         pass
    return render(req,'blogSite/PostDetail.html',{
                'postData': requiredPost
            })