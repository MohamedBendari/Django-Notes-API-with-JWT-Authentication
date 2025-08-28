from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NoteViewSet  # تأكد من وجود هذا الـ ViewSet في notes.views

router = DefaultRouter()
router.register('', NoteViewSet, basename='note')

urlpatterns = router.urls
