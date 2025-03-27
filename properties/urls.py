from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OwnerViewSet, PropertyViewSet, FeedbackViewSet

router = DefaultRouter()
router.register(r'owners', OwnerViewSet)
router.register(r'properties', PropertyViewSet)
router.register(r'feedback', FeedbackViewSet)

urlpatterns = [
    path('', include(router.urls)),
]