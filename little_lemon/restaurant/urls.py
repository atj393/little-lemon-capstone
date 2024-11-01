from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MenuViewSet, BookingViewSet

router = DefaultRouter()
router.register(r"menu", MenuViewSet)
router.register(r"bookings", BookingViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("admin/", admin.site.urls),
    path("api/", include("restaurant.urls")),
    path(
        "registration/", include("rest_framework.urls")
    ),  # Use DRF's built-in registration
    path("token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
