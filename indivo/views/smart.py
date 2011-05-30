"""
SMArt Views for Indivo
"""

from indivo.lib import utils
from base import *
from lxml import etree

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

def smart_demographics(request, record):
    # parse the demographics
    demographics_doc = etree.fromstring(record.demographics.content)
    
    # exploit the fact that demographics is a bunch of name-value pairs
    # remove the namespace, create a python dir, woohoo
    demographics = dict([(c.tag.replace('{http://indivo.org/vocab/xml/documents#}',''),c.text) for c in demographics_doc.getchildren()])
    
    # add name info
    demographics['name'] = record.label

    return render_template('smart_demographics', {'demographics': demographics})

def smart_lab_results(request, record):
    # FIXME: do lab results here
    lab_results = []
    return render_template('smart_lab_results', {'lab_results' : lab_results})
