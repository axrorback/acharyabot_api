from rest_framework.viewsets import ReadOnlyModelViewSet

from .models import (
    AdmissionProcess,
    TuitionFee,


)



from .serializers import (
    AdmissionProcessListSerializer,
    AdmissionProcessDetailSerializer,
   TuitionFeeSerializer
)


class AdmissionProcessViewSet(ReadOnlyModelViewSet):
    queryset = AdmissionProcess.objects.all()

    lookup_field = "process_type"

    def get_serializer_class(self):
        if self.action == "list":
            return AdmissionProcessListSerializer

        return AdmissionProcessDetailSerializer

class TuitionFeeViewSet(
    ReadOnlyModelViewSet
):
    queryset = TuitionFee.objects.select_related(
        "faculty"
    )

    serializer_class = TuitionFeeSerializer