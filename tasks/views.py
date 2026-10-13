from django.shortcuts import render

from rest_framework.generics import CreateAPIView,ListCreateAPIView,RetrieveUpdateDestroyAPIView,ListAPIView
from rest_framework import authentication,permissions
from tasks.serializer import UserSerializer,TaskSerializer
from tasks.models import Task
from tasks.permission import OwnerOnly
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.utils import timezone
from datetime import timedelta

# Create your views here.

class SignUpView(CreateAPIView):
    serializer_class=UserSerializer

class LogOutView(CreateAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]

    def post(self,request):
        Token.objects.filter(user=self.request.user).delete()

        return Response({"MESSAGE":"logout successful"})
    
  

class TaskListCreateView(ListCreateAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[permissions.IsAuthenticated]
    serializer_class=TaskSerializer
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

class TaskRetrieveUpdateDeleteView(RetrieveUpdateDestroyAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes=[OwnerOnly]
    serializer_class=TaskSerializer

    def get_queryset(self):
        return Task.objects.all()

    def perform_update(self, serializer):
        task=serializer.save()
        if task.status=="completed":
            task.completed_at=timezone.now()
            task.save(update_fields=["completed_at"])
        else:
            task.completed_at=None
            task.save(update_fields=["completed_at"])

class StreakView(ListAPIView):
    authentication_classes=[authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        completed_tasks = Task.objects.filter(user=request.user,status="completed",completed_at__isnull=False).order_by("-completed_at")

        dates = []
        for task in completed_tasks:
            date = timezone.localtime(task.completed_at).date()

            if date not in dates:
                dates.append(date)

        streak = 0
        today = timezone.localdate()
        for date in dates:
            if date == today - timedelta(days=streak):
                streak += 1
            else:
                break

        return Response({"study_streak": streak})


    

    

