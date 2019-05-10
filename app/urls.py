from django.urls import path

from . import views

urlpatterns = [

    path('',views.send),
    path('index/',views.index),
    

]
# index(repeat=1,repeat_until=None)
