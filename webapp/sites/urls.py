from django.conf.urls import url

from sites import views

urlpatterns=[

    url(r'^signup$',views.Signup,name="Signup"),
    url(r'^signin$',views.Signin,name="Signin"),
    url(r'^dashBoard$',views.dashBoard,name="dashBoard"),
    url(r'^signout$',views.Signout,name="Signout"),

]