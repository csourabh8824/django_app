from django import forms
from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


@login_required(login_url='/')
def logout_view(request):
    #used to logout

    logout(request)
    return render(request,'logout/logout_page.html')


@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    '''
    This view displays the home page after successfull login.
    '''
    template_name = 'login/homepage.html'
