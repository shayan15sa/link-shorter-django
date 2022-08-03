from django.urls import path
from . import views
urlpatterns = [
    path("",views.main_page),
    path("short/",views.shorter),
    path("s/<s>",views.showShort)
]
