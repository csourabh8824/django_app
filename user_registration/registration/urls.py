from django.urls import path, include
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required

from . import views as registration_view

urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='login/login_page.html',\
        redirect_authenticated_user=True)),
    path('accounts/', include('django_registration.backends.one_step.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('home/', registration_view.HomeView.as_view(), name = "homepage"),
    path('loggedout/',registration_view.logout_view,name = "logout"),
]
