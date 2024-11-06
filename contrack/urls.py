from django.urls import path
from contrack import views

urlpatterns = [
    path('', views.ContrackView.as_view()),
]