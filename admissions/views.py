from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import AdmissionProcess
from .serializers import (
    AdmissionProcessListSerializer,
    AdmissionProcessDetailSerializer,
)


class AdmissionProcessViewSet(ReadOnlyModelViewSet):
    queryset = AdmissionProcess.objects.all()

    lookup_field = "process_type"

    def get_serializer_class(self):
        if self.action == "list":
            return AdmissionProcessListSerializer

        return AdmissionProcessDetailSerializer

