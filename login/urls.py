from django.urls import URLPattern, path

from . import views


urlpatterns=[

    path('',views.index,name='index'),
    path('otp_check',views.otp_check,name='otp_check'),
]