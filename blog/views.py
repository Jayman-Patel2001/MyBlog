from django.shortcuts import render , HttpResponse , redirect
from .models import Post , BlogComment
from django.contrib import messages
from django.contrib.auth.models import User
from blog.templatetags import extras

def blogHome(request):
    allposts = Post.objects.all()
    context = {'allposts':allposts}
    return render(request , 'blog/blogHome.html' , context)

def blogPost(request, slug): 
    post=Post.objects.filter(slug=slug).first()
    comments= BlogComment.objects.filter(post=post , parent=None)
    replies = BlogComment.objects.filter(post=post).exclude(parent=None)
    replydict = {}

    for reply in replies:
        if reply.parent.sno not in replydict.keys():
            replydict[reply.parent.sno] = [reply]
        else:
            replydict[reply.parent.sno].append(reply)

    context={'post':post, 'comments': comments , 'user':request.user, 'replydict':replydict}
    return render(request, "blog/blogPost.html", context)

def postComment(request):
    if request.method == "POST":
        comment=request.POST.get('comment' , '')
        user=request.user
        postSno =request.POST.get('postSno' , '')
        post= Post.objects.get(sno=postSno)
        parentSno= request.POST.get('parentSno' , '')

        if len(comment) < 1:
            messages.warning(request , 'Comment cant be empty')

        else:

            if parentSno=="":
                comment=BlogComment(comment= comment, user=user, post=post)
                comment.save()               

            else:
                parent= BlogComment.objects.get(sno=parentSno)
                comment=BlogComment(comment= comment, user=user, post=post , parent=parent)
                comment.save()               
        
    return redirect(f"/blog/{post.slug}")