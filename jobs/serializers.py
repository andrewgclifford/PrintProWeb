from rest_framework import serializers
from .models import Job, JobFile, Comment

class JobFileSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobFile
        fields = ['id', 'file', 'file_type', 'uploaded_by', 'uploaded_at']

class CommentSerializer(serializers.ModelSerializer):
    user_name = serializers.CharField(source='user.get_full_name', read_only=True)
    
    class Meta:
        model = Comment
        fields = ['id', 'content', 'user', 'user_name', 'created_at']

class JobSerializer(serializers.ModelSerializer):
    files = JobFileSerializer(many=True, read_only=True)
    comments = CommentSerializer(many=True, read_only=True)
    client_name = serializers.CharField(source='client.company_name', read_only=True)
    assigned_to_name = serializers.CharField(source='assigned_to.get_full_name', read_only=True)
    
    class Meta:
        model = Job
        fields = '__all__' 