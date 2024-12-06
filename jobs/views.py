from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.utils import timezone
from .models import Job, JobFile, Comment
from .serializers import JobSerializer, JobFileSerializer, CommentSerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = Job.objects.all()
        status = self.request.query_params.get('status', None)
        priority = self.request.query_params.get('priority', None)
        
        if status:
            queryset = queryset.filter(status=status)
        if priority:
            queryset = queryset.filter(priority=priority)
            
        if self.request.user.user_type == 'client':
            queryset = queryset.filter(client__user=self.request.user)
            
        return queryset

    @action(detail=True, methods=['post'])
    def upload_file(self, request, pk=None):
        job = self.get_object()
        file_serializer = JobFileSerializer(data=request.data)
        
        if file_serializer.is_valid():
            file_serializer.save(job=job, uploaded_by=request.user)
            return Response(file_serializer.data)
        return Response(file_serializer.errors, status=400)

    @action(detail=True, methods=['post'])
    def add_comment(self, request, pk=None):
        job = self.get_object()
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(job=job, user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors, status=400)

    @action(detail=True, methods=['post'])
    def approve_proof(self, request, pk=None):
        job = self.get_object()
        job.proof_approved = True
        job.proof_approved_at = timezone.now()
        job.proof_approved_by = request.user
        job.save()
        return Response({'status': 'proof approved'})

    @action(detail=True, methods=['post'])
    def update_status(self, request, pk=None):
        job = self.get_object()
        new_status = request.data.get('status')
        if new_status in dict(Job.STATUS_CHOICES):
            job.status = new_status
            job.save()
            return Response({'status': 'updated'})
        return Response({'error': 'Invalid status'}, status=400) 