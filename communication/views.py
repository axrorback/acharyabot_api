from rest_framework.viewsets import ReadOnlyModelViewSet
from .models import FAQ
from .serializers import FAQListSerializer,FAQDetailSerializer

class FAQViewSet(ReadOnlyModelViewSet):
    queryset = FAQ.objects.filter(is_active=True)

    def get_serializer_class(self):
        if self.action == "list":
            return FAQListSerializer

        return FAQDetailSerializer