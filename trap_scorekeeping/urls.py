"""trap_scorekeeping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""


from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.render_index, name='index'),
    url(r'^score_entry/(?P<model_id>[0-9]+)', views.render_score_entry, name='score_entry'),
    url(r'^round_entry', views.render_round_entry, name='round_entry'),
    url(r'^ack_entry/(?P<model_id>[0-9]+)', views.render_ack_entry, name='ack_entry')
    # url(r'^shotgun_entry', views.render_shotgun_entry, name='shotgun_entry')
]
