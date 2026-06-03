from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework import generics

from drf_spectacular.utils import extend_schema, OpenApiParameter

from .models import FAQ, ContactMessage
from .serializers import (
    FAQListSerializer,
    FAQDetailSerializer,
    ContactMessageSerializer
)

@extend_schema(
    parameters=[
        OpenApiParameter(
            name="lang",
            type=str,
            location=OpenApiParameter.QUERY,
            description="Language selector: uz | en | ru",
            required=False,
        )
    ]
)
class FAQViewSet(ReadOnlyModelViewSet):
    queryset = FAQ.objects.all().order_by("order")

    def get_serializer_class(self):
        if self.action == "list":
            return FAQListSerializer
        return FAQDetailSerializer


@extend_schema(
    request=ContactMessageSerializer,
    responses={201: ContactMessageSerializer},
    description="Send contact message from frontend or Telegram bot"
)
class ContactMessageCreateAPIView(generics.CreateAPIView):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer