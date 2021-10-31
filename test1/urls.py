from django.urls import path
from . import views
from rest_framework.routers import SimpleRouter 
from django.conf import settings
from django.conf.urls.static import static


router = SimpleRouter()

router.register('clients',views.ClientViewSet,basename='clients')


# URLConf
urlpatterns = router.urls


if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)


# # URLConf
# urlpatterns = [
#     path('hello/', views.say_hello)
# ]
