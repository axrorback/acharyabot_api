from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register("processes",AdmissionProcessViewSet,basename="processes")

router.register("fees",TuitionFeeViewSet,basename="fees")

router.register("scholarships",ScholarshipViewSet,basename="scholarships")

router.register("grants",GrantViewSet,basename="grants")

router.register("documents",RequiredDocumentViewSet,basename="documents")

urlpatterns = router.urls