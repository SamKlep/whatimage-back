from .views import ImageviewSet
from rest_framework import routers
from django.urls import path, include
app_name = 'api-images'

router = routers.DefaultRouter()
router.register(r'images', ImageviewSet)

urlpatterns = [
    path('', include(router.urls))
]