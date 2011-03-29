"""
SMArt Views for Indivo
"""

from indivo.lib import utils
from base import *


def smart_app_setup(request, record, smart_app_email):
    """
    setup a smart app
    """
    smart_app = SmartApp.objects.get(email = smart_app_email)
    SmartRecordInstalledApp.objects.get_or_create(app = smart_app, record=record)
    return DONE


def smart_app_remove(request, record, smart_app_email):
    """
    remove a smart app
    """
    smart_app = SmartApp.objects.get(email = smart_app_email)
    SmartRecordInstalledApp.objects.get(app = smart_app, record=record).delete()
    return DONE



def smart_meds(request, record):
    meds = Medication.objects.filter(record = record)
    return render_template('smart_meds', {'meds' : meds})


def smart_problems(request, record):
    problems = Problem.objects.filter(record = record)
    return render_template('smart_problems', {'problems' : problems})
