from .import views
from django.urls import path
app_name= 'aasra'
urlpatterns = [
     path('',views.api,name='api'),
     path('<int:no>/',views.upvote,name='upvote'),
]


# Create your tests here.
