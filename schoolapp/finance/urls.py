from . import views
from django.urls import path
urlpatterns=[
    path("feecollection",views.feecollection),
    path("feecollectionreport",views.feeCollectionReport),
    path("feeduereport",views.feeDuesReport),
    path("",views.home)
]