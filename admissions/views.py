from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import (
    AdmissionProcess,
    TuitionFee,
    Grant,
    RequiredDocument
)

from .serializers import (
    AdmissionProcessListSerializer,
    AdmissionProcessDetailSerializer,
   TuitionFeeSerializer,
   GrantSerializer,
   RequiredDocumentSerializer
)


class AdmissionProcessViewSet(ReadOnlyModelViewSet):
    queryset = AdmissionProcess.objects.all()

    lookup_field = "process_type"

    def get_serializer_class(self):
        if self.action == "list":
            return AdmissionProcessListSerializer

        return AdmissionProcessDetailSerializer



class TuitionFeeViewSet(ReadOnlyModelViewSet):
    queryset = TuitionFee.objects.select_related("faculty")
    serializer_class = TuitionFeeSerializer



class GrantViewSet(ReadOnlyModelViewSet):
    queryset = Grant.objects.all()
    serializer_class = GrantSerializer


class RequiredDocumentViewSet(ReadOnlyModelViewSet):
    queryset = RequiredDocument.objects.all()
    serializer_class = RequiredDocumentSerializer