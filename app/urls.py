from django.urls import path
from .views import *
urlpatterns = [
    path('hello', FirstTask, name="first-task" ),
    path('users', SecondTask, name="second-task"),
    path('new_user',ThirdTask, name="user_form"),
    path('api/create/', ThirdTash1, name="create_user_api"),
    path('users/<int:id>', ForthTask, name="Fetch-user-details"),
]
