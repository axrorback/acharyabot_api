from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import FAQViewSet,ContactMessageCreateAPIView

router = DefaultRouter()
router.register("faq",FAQViewSet,basename="faq")

urlpatterns = router.urls + [
    path("contact/",ContactMessageCreateAPIView.as_view(),name="contact-create"),
]