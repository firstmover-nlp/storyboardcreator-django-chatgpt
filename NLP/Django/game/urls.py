from django.urls import path
from . import views

urlpatterns = [
    path("", views.gamepage, name="gamepage"),
    #광고
    path("denis", views.denis, name="denis"),
    path("remy", views.remy, name="remy"),
    #숏폼
    path("mylo", views.mylo, name="mylo"),
    path("eugene", views.eugene, name="eugene"),
    path("camila", views.camila, name="camila"),
    #광고
    path("dave", views.dave, name="dave"),
    
    path("threadtest", views.threadtest, name="threadtest"),
    path("creator", views.creator, name="creator")
    

]