from django.conf.urls import url

from employee import views

urlpatterns=[

    url(r'^hello$',views.helloDjango,name="hello"),
    url(r'^hello_python$',views.hellopython,name="hello_python"),
    url(r'^nav1$', views.nav1, name="nav1"),
    url(r'^nav2$', views.nav2, name="nav2"),
    #url(r'^login$', views.login, name="login"),
    #url(r'^signup$', views.signup, name="signup"),
    url(r'^formTest$', views.formTest, name="form"),
    url(r'^create$',views.create,name='create'),
    url(r'^index$',views.index,name='index'),
    url(r'^update/(?P<pk>[0-9]+)$',views.update,name='update'),  #()-block (a+b)+(c) <pk> primarykey p is mandidatory
    url(r'^delete/(?P<pk>[0-9]+)$',views.delete,name='delete'),
    url(r'^view/(?P<pk>[0-9]+)$',views.view,name='view'),

    url(r'^createteachcer$',views.teacher_create,name='createteacher'),
    url(r'^teacherindex$',views.teacher_index,name='teacherindex'),
    url(r'^tupdate/(?P<pk>[0-9]+)$',views.teacher_update,name='teacherupdate'),  #()-block (a+b)+(c) <pk> primarykey p is mandidatory
    url(r'^tdelete/(?P<pk>[0-9]+)$',views.teacher_delete,name='teacherdelete'),
    url(r'^tview/(?P<pk>[0-9]+)$',views.teacher_view,name='teacherview'),



    url(r'^create_sgpg$',views.sgpg,name='createsgpg'),
    url(r'^sgpgindex$',views.sgpg_index,name='sgpgindex'),

]
