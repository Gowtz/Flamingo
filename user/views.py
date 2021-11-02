from django.shortcuts import render, redirect, reverse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import (LoginView, LogoutView, 
                                        PasswordChangeView, 
                                        PasswordResetView, 
                                        PasswordResetConfirmView)
from django.views.generic import CreateView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from .forms import UserRegistrationForm, UserUpdateForm, ProfileUpdateForm
from blog.models import BlogModel



def register(request):
    if request.user.is_authenticated:
        name = str(request.user.is_authenticated)
        messages.success(
                request, f'{name} is already logged in. Logout to create a new user.')
        return redirect('user:login') 
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            user = form.save(commit=False)
            user.email = email
            user.save()
            messages.success(
                request, f'Your registration for {email} is successfully created.')
            return redirect('user:login')
    else:
        form = UserRegistrationForm()

    content = {'form': form}
    return render(request, 'user/registration.html', content)


class UserLogin(LoginView):
    template_name = 'user/login.html'
    redirect_authenticated_user = True

    def dispatch(self, request, *args, **kwargs):
        if self.redirect_authenticated_user and self.request.user.is_authenticated:
            messages.success(
                request, 'Already an account is logged in, Please logout to login with new account.')
        return super().dispatch(request, *args, **kwargs)


class UserLogout(LogoutView):
    template_name = 'user/logout.html'

    def dispatch(self, request, *args, **kwargs):
        messages.success(request, 'You have been logged out successfully..')
        return super().dispatch(request, *args, **kwargs)


@login_required
def profile(request):
    posts = BlogModel.objects.filter(user=request.user).order_by('-id')
    content = {'posts':posts}
    return render(request, 'user/profile.html', content)


@login_required
def update_profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        
        if u_form.is_valid() and p_form.is_valid():
            email = u_form.cleaned_data.get('username')
            user = u_form.save(commit=False)
            user.email = email
            user.save()
            p_form.save()
            messages.success(request, 'Profile has been updated successfully')
            return redirect('user:profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    content = {'u_form':u_form,
                'p_form':p_form,
                }
    return render(request,'user/profile_update.html',content)



class UserPasswordChangeView(SuccessMessageMixin, PasswordChangeView):
    success_url = reverse_lazy('user:profile')
    template_name="user/password_change.html"
    success_message = "Password has been changed successfully"


class UserPasswordResetView(SuccessMessageMixin, PasswordResetView):
    success_url = reverse_lazy('user:login')
    template_name='user/password_reset_form.html'
    email_template_name = 'user/password_reset_email.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            em = form.cleaned_data.get('email')
            if User.objects.filter(email= em).exists():
                messages.success(request, f'A link to reset your account password has been sent to {em}.')
                return self.form_valid(form)
            else:
                messages.warning(request, f'Entered email id:- {em} is not registered. Please check with the mail id or register your account.')
                return self.form_invalid(form)

        else:
            return self.form_invalid(form)


class UserPasswordResetConfirmView(SuccessMessageMixin, PasswordResetConfirmView):
    success_url = reverse_lazy('user:login')
    template_name = 'user/password_reset_confirm.html'

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            messages.success(request, f'Your password reset successful')
            return self.form_valid(form)
        else:
            return self.form_invalid(form)