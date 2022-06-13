from django.urls import path
from . import views


urlpatterns = [
    path('form/',views.showfromdata),
    path('thanks/',views.thanks),
]
