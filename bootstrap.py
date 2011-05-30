
from indivo.models import *
from django.conf import settings

# add some smart apps
SmartApp.objects.create(
    email = 'medlist@apps.smart.org',
    consumer_key = 'medlist@apps.smart.org',
    name = 'SMART MedList',
    start_url_template = 'http://sample-apps.smartplatforms.org/framework/med_list/bootstrap.html',
    has_ui = True)


SmartApp.objects.create(
    email = 'smart-problems@apps.smart.org',
    consumer_key = 'problems@apps.smart.org',
    name = 'SMART Problems',
    start_url_template = 'http://sample-apps.smartplatforms.org/framework/problem_list/bootstrap.html',
    has_ui = True)


SmartApp.objects.create(
    email = 'gotstatins@apps.smart.org',
    consumer_key = 'gotstatins@apps.smart.org',
    name = 'Got Statins?',
    start_url_template = 'http://sample-apps.smartplatforms.org/framework/got_statins/bootstrap.html',
    has_ui = True)

SmartApp.objects.create(
    email = 'cardio_risk_viz@apps.smartplatforms.org',
    consumer_key = 'cardio_risk_viz@apps.smartplatforms.org',
    name = 'Cardiac Risk',
    start_url_template = 'http://sample-apps.smartplatforms.org/framework/cardio_risk_viz/bootstrap.html',
    has_ui = True)


