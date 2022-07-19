from django.urls import path

from . import views

app_name = 'problems'
urlpatterns = [
    path('<int:problem_id>', views.details, name='details'),
]