from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.views import (
    ProfileViewSet, ExpertiseViewSet, ProjectViewSet,
    SkillViewSet, FocusViewSet, CareerViewSet
)

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'expertise', ExpertiseViewSet)
router.register(r'projects', ProjectViewSet)
router.register(r'skills', SkillViewSet)
router.register(r'focus', FocusViewSet)
router.register(r'career', CareerViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
