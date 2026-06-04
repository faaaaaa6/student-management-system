from django.urls import path
from .import views

urlpatterns = [
    path("delete_student/<int:pk>/",views.delete_student,name="delete_student")
]
