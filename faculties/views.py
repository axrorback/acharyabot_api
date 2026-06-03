from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import Faculty
from .serializers import (
    FacultyListSerializer,
    FacultyDetailSerializer
)


class FacultyViewSet(ReadOnlyModelViewSet):
    queryset = Faculty.objects.filter(
        is_active=True
    )

    lookup_field = "slug"

    def get_serializer_class(self):
        if self.action == "list":
            return FacultyListSerializer

        return FacultyDetailSerializer