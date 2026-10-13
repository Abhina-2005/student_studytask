from rest_framework import serializers
from tasks.models import User,Task
from django.utils import timezone

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["username","phone","email","password"]
        read_only_fields=["id"]
    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
    
    def validate_phone(self,value):
        if len(value)!=10:
            raise serializers.ValidationError("phone number must be exactly 10 digits")
        return value

class TaskSerializer(serializers.ModelSerializer):
    due_status=serializers.SerializerMethodField()
    class Meta:
        model=Task
        fields="__all__"
        read_only_fields=["id","created_at","user","completed_at"]

    def get_due_status(self,obj):
        today=timezone.localdate()
        if obj.status=="completed":
            return "Completed"
        elif obj.due_date<today:
            return "Overdue"
        elif obj.due_date==today:
            return "Due today"
        else:
            return "Upcoming"

