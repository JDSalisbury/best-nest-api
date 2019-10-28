from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('box', BoxViewSet)
router.register('task', TaskViewSet)
router.register('user', UserViewSet)

urlpatterns = [
] + router.urls
