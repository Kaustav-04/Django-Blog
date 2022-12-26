from tkinter import N
from django.shortcuts import render
from datetime import date
from .models import Post
from .form import CommentForm
# Create your views here.


def FirstPage(req):
    filteredPost = Post.objects.all().order_by('-date')[:3]
    return render(req, 'blogSite/index.html', {
        'posts': filteredPost
    })


def AllPost(req):
    Posts = Post.objects.all().order_by('-date')
    return render(req, 'blogSite/AllPost.html', {
        'Posts': Posts
    })


def PostDetails(req, slug):
    commentForm = CommentForm()
    stored_post = req.session.get('stored_post')
    if req.method == 'GET':
        requiredPost = Post.objects.get(slug=slug)
        # for i in posts:
        #     if i['slug'] == slug:
        #         return render(req,'blogSite/PostDetail.html',{
        #             'postData': i
        #         })
        #     else:
        #         pass
        saved_for_later = False
        if stored_post:
            if str(requiredPost.id) in stored_post:
                saved_for_later = True

        return render(req, 'blogSite/PostDetail.html', {
            'postData': requiredPost,
            'form': commentForm,
            'comments': requiredPost.comment.all().order_by('-id'),
            'saved_for_later': saved_for_later
        })

    elif req.method == 'POST':
        comment_form = CommentForm(req.POST)
        post = Post.objects.get(slug=slug)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()



        return render(req, 'blogSite/PostDetail.html', {
            'postData': post,
            'form': commentForm,
            'comments': post.comment.all().order_by('-id'),
            'saved_for_later': saved_for_later
        })


def readLater(req):
    stored_post = req.session.get('stored_post')
    if req.method == 'GET':
        if (stored_post is None) or (len(stored_post) == 0):
            has_post = False
            return render(req, 'blogSite/readLater.html', {
                'Posts': [],
                'has_post': has_post
            })

        else:
            has_post = True
            filtered_post = Post.objects.filter(pk__in=stored_post)
            return render(req, 'blogSite/readLater.html', {
                'Posts': filtered_post,
                'has_post': has_post
            })

    elif req.method == 'POST':
        if stored_post is None:
            stored_post = []

        post_id = req.POST['post_id']

        if post_id not in stored_post:
            stored_post.append(post_id)
        else:
            stored_post.remove(post_id)

        req.session['stored_post'] = stored_post
        has_post = True
        filtered_post = Post.objects.filter(pk__in=stored_post)
        return render(req, 'blogSite/readLater.html', {
            'Posts': filtered_post,
            'has_post': has_post
        })
