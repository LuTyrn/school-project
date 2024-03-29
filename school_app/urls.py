from django.urls import path

from . import views

urlpatterns = [
    path('hello-world', views.hello_world, name="hello-world"),
    path('welcome', views.welcome_to_school, name="welcome_to_school"),
    path('subjects', views.list_subjects, name="list_subjects"),
    path('subjects/<int:pk>', views.subject_detail, name="subject_detail")   # <int:pk> query parametr (integer:promena pk)
]
