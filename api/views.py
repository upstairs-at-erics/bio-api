from django.shortcuts import render


from rest_framework import viewsets
from .models import Profile, Expertise, Project, Skill, Focus, Career
from .serializers import (
    ProfileSerializer, ExpertiseSerializer, ProjectSerializer,
    SkillSerializer, FocusSerializer, CareerSerializer
)


# Create your views here.
class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ExpertiseViewSet(viewsets.ModelViewSet):
    queryset = Expertise.objects.all()
    serializer_class = ExpertiseSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillSerializer

class FocusViewSet(viewsets.ModelViewSet):
    # Sorts by created_at, newest first
    queryset = Focus.objects.all().order_by('-created_at')
    serializer_class = FocusSerializer

class CareerViewSet(viewsets.ModelViewSet):
    # Sorts by id descending (assuming higher ID = newer entry)
    # If you add a 'created_at' to the Career model, change this to '-created_at'
    queryset = Career.objects.all().order_by('-id')
    serializer_class = CareerSerializer

