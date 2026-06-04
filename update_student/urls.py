from django.urls import path
from .import views

urlpatterns = [
    path("update_student/<int:pk>/",views.update_student,name="update_student")
]
