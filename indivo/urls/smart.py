from django.conf.urls.defaults import *

from indivo.views import *
from indivo.lib.utils import MethodDispatcher

urlpatterns = patterns(
    '',
    
    # app setup
    (r'^records/(?P<record_id>[^/]+)/apps/(?P<smart_app_email>[^/]+)/setup', smart_app_setup),
    (r'^records/(?P<record_id>[^/]+)/apps/(?P<smart_app_email>[^/]+)/remove', smart_app_remove),

    # smart demographics
    (r'^records/(?P<record_id>[^/]+)/demographics$', smart_demographics),
    
    # smart meds call
    (r'^records/(?P<record_id>[^/]+)/medications/$', smart_meds),

    # smart problems call
    (r'^records/(?P<record_id>[^/]+)/problems/$', smart_problems),

    # smart lab_results call
    (r'^records/(?P<record_id>[^/]+)/lab_results/$', smart_lab_results),
)
