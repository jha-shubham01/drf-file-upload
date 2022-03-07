from rest_framework import routers

from .views import FileViewSet, ImageViewSet

router = routers.DefaultRouter()
router.register('file', FileViewSet)
router.register('image', ImageViewSet)

urlpatterns = router.urls