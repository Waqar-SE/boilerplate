from rest_framework.routers import DefaultRouter
from accounts.api import viewsets

router = DefaultRouter()

router.register("signup", viewsets.SignUpViewSet, basename="signup")
router.register("users", viewsets.UserModelViewSet, basename="users")
router.register("profiles", viewsets.ProfileModelViewSet, basename="profiles")

urlpatterns = router.urls
