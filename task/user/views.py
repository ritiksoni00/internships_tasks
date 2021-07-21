from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from django.contrib import messages
from . forms import AuthForm, PostForm
from . models import User
from django.core.exceptions import ObjectDoesNotExist



def auth_form(request):
    auth_form = AuthForm()
    if request.method == 'POST':
        auth_form = AuthForm(request.POST)

        if auth_form.is_valid():
            user_name = request.POST['username']
            try:
                user = User.objects.get(username=user_name)
            except ObjectDoesNotExist:
                messages.error(request,'username or password not correct')
            
                return render(request,'home.html' ,{ 'auth_form': auth_form} )
            if user:
                con = {'user' : user_name}
                return redirect('show_post_form')
            else:           
                return redirect('auth_form')
    return render(request, 'home.html' ,{ 'auth_form': auth_form})


def show_post_form(request):
    form = PostForm()
    return render(request, 'post.html',{'form': form})
