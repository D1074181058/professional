"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from myapp import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
    url(r'^pig/',views.pig),
    url(r'^beef/',views.beef),
    url(r'^chicken/',views.chicken),
    url(r'^lamb/',views.lamb),
    url(r'^seafood/',views.seafood),
    url(r'^agaricus/',views.agarigus),
    url(r'^vegetables/',views.vegetables),

    url(r'^signup/',views.signup),
    url(r'^login/',views.login),
    url(r'^captcha/',include('captcha.urls')),
    url(r'^logout/',views.logout),

    #url(r'^login1/$',views.login1),
    #url(r'^login2/$',views.login2),
    #url(r'^hello/(\w+)/',hello),



]
