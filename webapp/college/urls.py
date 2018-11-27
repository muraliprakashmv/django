from django.conf.urls import url

from college import views

urlpatterns=[

    url(r'^hello_world$',views.hello_World,name="hello"),
]