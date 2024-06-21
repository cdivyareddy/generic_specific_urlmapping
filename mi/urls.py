from django.urls import path
from mi.views import *
app_name="anything"
urlpatterns=[
    path('rohith/',rohith,name='rohith'),
    path('captain/',captain,name="captain")
]