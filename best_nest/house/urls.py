from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('house', HouseViewSet)
router.register('task', TaskViewSet)

urlpatterns = [
] + router.urls
