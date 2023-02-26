from . import views
from django.urls import path,include, re_path
urlpatterns = [

    re_path(r'^$',views.home, name='home'),

]
