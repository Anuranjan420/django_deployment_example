



from django.contrib import admin
from django.urls import path,re_path,include
from basic_app import views

    #Template tagging
app_name='basic_app'

urlpatterns = [
        re_path(r'^relative/$',views.relative,name='relative'),
        re_path(r'^other/$',views.other,name='other'),
        #re_path(r'^basic_app/',include('basic_app.urls')),
        #re_path(r'^admin/', admin.site.urls),
    ]
