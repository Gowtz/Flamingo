from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import BlogUpdateForm
from .models import BlogModel
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def add_blog(request):
    if not(request.user.is_authenticated):
        messages.warning(
                request, f'Please login to add a Post')
        return redirect('user:login') 
    if request.method == "POST":
        form = BlogUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            messages.success(request, 'Added Post successfully')
            return redirect('web:home')
    else:
        form = BlogUpdateForm(instance=request.user)

    content = {'form':form}
    return render(request,'blog/posting.html',content)


@login_required
def edit_blog(request, pk):
    post = BlogModel.objects.get(pk=pk)
    if request.method=='POST':
        form = BlogUpdateForm(request.POST,request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('user:profile')
        else:
            form = BlogUpdateForm(instance=post)
    else:
        form = BlogUpdateForm(instance=post)

    content = {'form':form}
    return render(request,'blog/posting.html',content)


@login_required
def delete_blog(request, pk):
    post = BlogModel.objects.get(pk=pk)
    post.delete()
    return redirect('user:profile')
