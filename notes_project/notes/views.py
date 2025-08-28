from rest_framework import viewsets, permissions
from .models import Note
from .serializers import NoteSerializer

class NoteViewSet(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # بس الملاحظات الخاصة بالمستخدم الحالي
        return Note.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        # تعيين صاحب الملاحظة تلقائيًا
        serializer.save(owner=self.request.user)
