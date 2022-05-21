from django.urls import path

from courses.views import courses
from .views import home, about, courses

urlpatterns = [
    path('home/',home),
    path('about/',about),
    path('courses/',courses)

]
