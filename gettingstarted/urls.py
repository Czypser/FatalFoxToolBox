from django.conf.urls import url
from django.urls import include, path

from django.contrib import admin
admin.autodiscover()

import hello.views

# Examples:
# url(r'^$', 'gettingstarted.views.home', name='home'),
# url(r'^blog/', include('blog.urls')),

urlpatterns = [
    url(r'^$', hello.views.index, name='index'),
    url(r'^db', hello.views.db, name='db'),
    path('admin/', admin.site.urls),
	path('eqparse/', include('EQParse.urls')),
]
