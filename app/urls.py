from .views import LaptopViewSet
from rest_framework import routers


router = routers.SimpleRouter()
router.register('shiv', LaptopViewSet)
urlpatterns = router.urls
