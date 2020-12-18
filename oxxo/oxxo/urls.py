from django.contrib import admin
from django.urls import path
from rest_framework.routers import DefaultRouter
from producto.views import ChelaViewSet

router = DefaultRouter()
router.register(f'producto', ChelaViewSet)

urlpatterns = router.urls
urlpatterns += [
    path('admin/', admin.site.urls),

]
