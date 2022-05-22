from django.urls import path

from courses.views import courses
from .views import home, contact, courses

urlpatterns = [
    path('home/',home),
    path('contact/',contact),
    path('courses/',courses)

]
