from django.conf import settings
from indivo.models import *
from string import Template
import re, sys, os
from django.utils import simplejson
import urllib2

def sub(str, var, val):
    return str.replace("{%s}"%var, val)

def LoadApp(app):
  print app

  if not app.startswith("http"):
      s = open(app)
  else:
      s = urllib2.urlopen(app)

  r = simplejson.loads(s.read())
  s.close() 

  assert r["mode"] == "ui", "Can only import UI SMART apps into Indivo"

  SmartApp.objects.create(
      email = r["id"],
      consumer_key = r["id"],
      name = r["name"],
      start_url_template = r["activities"]["main"],
      has_ui = True)

if __name__ == "__main__":
    import string
    for v in sys.argv[1:]:
        print "Loading app: %s"%v
        LoadApp(v)


