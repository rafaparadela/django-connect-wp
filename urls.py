from django.conf.urls.defaults import *

urlpatterns = patterns('',

    (r'^last_post', 'myproject.myapp.views.last_post'),
    
)
