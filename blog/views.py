from django.shortcuts import render,  redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from . models import Blog
from django.contrib import messages
from . forms import Edit_blog


# Create your views here.

def blog(request):
    blog = Blog.objects.all().order_by('-id')
    paginator = Paginator(blog,4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #print('Blog=',blog)
   # print()
   # print('Paginator=', paginator)
    #print()
    #print('Page_number=', page_number)
   # print()
   # print('Blog_per_page=', blog_per_page)
   # print()
    
    return render(request,'blog/blogs.html',{'page_obj':page_obj}) 

def addpost(request):
    if request.method == "POST":
        title = request.POST.get('title')
        desc = request.POST.get('desc')
        print(title,desc)
        blog = Blog(title=title,desc=desc,user_id=request.user)
        blog.save()
        messages.success(request,'Your Blog has been Posted successfully.')
        return redirect('blog')
    return render(request,'blog/addpost.html')

def blog_details(request,id):
    blog = Blog.objects.get(id=id)
    context = {'blog':blog}
    return render(request,'blog/blog_details.html',context)

def delete_post(request,id):
    blog = Blog.objects.get(id=id)
    blog.delete()
    messages.success(request,'Post has been deleted successfully.') 
    return redirect('blog')   

def edit_post(request,id):
    blog = Blog.objects.get(id=id)
    editpost = Edit_blog(instance=blog)
    if request.method == 'POST':
        form = Edit_blog(request.POST,instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request,'post has been updated')
            return redirect('blog')
    context = {'edit_post':editpost}
    return render(request,'blog/edit_post.html',context)  

def search(request):
    query = request.GET['query']
    blog = Blog.objects.filter(desc__icontains=query) or Blog.objects.filter(title__icontains=query)
    context = {'blogs':blog}
    
    return render(request,'blog/search.html',context)              