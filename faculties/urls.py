from rest_framework.routers import DefaultRouter
from .views import FacultyViewSet
router = DefaultRouter()

router.register("",FacultyViewSet,basename="faculties")

urlpatterns = router.urls