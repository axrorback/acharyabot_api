from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import generics

from .models import FAQ , ContactMessage
from .serializers import FAQListSerializer,FAQDetailSerializer, ContactMessageSerializer


class FAQViewSet(ReadOnlyModelViewSet):
    queryset = FAQ.objects.all().order_by("order")

    def get_serializer_class(self):
        if self.action == "list":
            return FAQListSerializer

        return FAQDetailSerializer

class ContactMessageCreateAPIView(generics.CreateAPIView):

    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer