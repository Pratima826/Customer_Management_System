from django.urls import path
from .views import*

# BASE URL = http://127.0.0.1:8000/CMS/cms/

urlpatterns=[
         path('cms/',view_cms),
         path('cusfrm/',view_customer),
         ]