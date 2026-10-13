"""
URL configuration for studytask project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from tasks.views import SignUpView
from rest_framework.authtoken.views import ObtainAuthToken
from tasks.views import TaskListCreateView
from tasks.views import TaskRetrieveUpdateDeleteView
from tasks.views import LogOutView
from tasks.views import StreakView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/register/",SignUpView.as_view()),
    path("api/token/",ObtainAuthToken.as_view()),
    path("api/tasks/",TaskListCreateView.as_view()),
    path("api/tasks/<int:pk>/",TaskRetrieveUpdateDeleteView.as_view()),
    path("api/logout/",LogOutView.as_view()),
    path("api/streak/",StreakView.as_view()),
]
