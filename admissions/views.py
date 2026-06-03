from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import (
    AdmissionProcess,
    TuitionFee,
    Grant,
    RequiredDocument,
    Scholarship
)

from .serializers import (
    AdmissionProcessListSerializer,
    AdmissionProcessDetailSerializer,
    TuitionFeeSerializer,
    GrantSerializer,
    RequiredDocumentSerializer,
    ScholarshipSerializer
)

@extend_schema(
    parameters=[
        OpenApiParameter(
            name="lang",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Language: uz | en | ru",
            required=False,
        )
    ]
)
class AdmissionProcessViewSet(ReadOnlyModelViewSet):
    queryset = AdmissionProcess.objects.all()
    lookup_field = "process_type"
    lookup_url_kwarg = "process_type"

    def get_serializer_class(self):
        if self.action == "list":
            return AdmissionProcessListSerializer
        return AdmissionProcessDetailSerializer

@extend_schema(
    parameters=[
        OpenApiParameter(
            name="lang",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Language: uz | en | ru",
            required=False,
        )
    ]
)
class TuitionFeeViewSet(ReadOnlyModelViewSet):
    queryset = TuitionFee.objects.select_related("faculty").all()
    serializer_class = TuitionFeeSerializer

@extend_schema(
    parameters=[
        OpenApiParameter(
            name="lang",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Language: uz | en | ru",
            required=False,
        )
    ]
)
class GrantViewSet(ReadOnlyModelViewSet):
    queryset = Grant.objects.all()
    serializer_class = GrantSerializer

@extend_schema(
    parameters=[
        OpenApiParameter(
            name="lang",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Language: uz | en | ru",
            required=False,
        )
    ]
)
class RequiredDocumentViewSet(ReadOnlyModelViewSet):
    queryset = RequiredDocument.objects.all()
    serializer_class = RequiredDocumentSerializer

@extend_schema(
    parameters=[
        OpenApiParameter(
            name="lang",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Language: uz | en | ru",
            required=False,
        )
    ]
)
class ScholarshipViewSet(ReadOnlyModelViewSet):
    queryset = Scholarship.objects.all()
    serializer_class = ScholarshipSerializer