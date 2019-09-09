from django.contrib import admin
from django.urls import path,include
#FROM DEMO IMPORT VIEWS.PY FILE
from . import views
#FROM VIEWS.PY IMPORT CLASS2
from .views import Another
# using router to register  our bookviewset as ' books'
from rest_framework import routers
from .views import BookViewSet

router = routers.DefaultRouter()
router.register('books', BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', views.function),
    # path('fbv', views.function),
    # path('cbv', Another.as_view()),
#for using router.urls must give include in  the path
    path('',include(router.urls))



]
