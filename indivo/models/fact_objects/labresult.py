"""
Indivo Model for Lab Results

2011-05-30
"""

from fact import Fact
from django.db import models
from django.conf import settings

class LabResult(Fact):
  date_measured         = models.DateTimeField()
  lab_name              = models.CharField(max_length=250, null=True)
  lab_address           = models.CharField(max_length=250, null=True)
  lab_type              = models.CharField(max_length=250, null=True)
  lab_comments          = models.TextField(null=True)

  # the lab test name, coded
  name                  = models.CharField(max_length=300, null=True)
  name_type             = models.CharField(max_length=250, null=True)
  name_value            = models.CharField(max_length=250, null=True)
  is_final              = models.NullBooleanField(null=True)

  # result
  result_value          = models.CharField(max_length=100, null=True)
  result_unit           = models.CharField(max_length=100, null=True)
  result_unit_type      = models.CharField(max_length=200, null=True)
  result_unit_value     = models.CharField(max_length=200, null=True)

  # abnormal flag?
  flag_type             = models.CharField(max_length=200, null=True)
  flag_value            = models.CharField(max_length=200, null=True)
  
  # ranges
  # we assume same unit as the result
  normal_range_minimum  = models.CharField(max_length=250, null=True)
  normal_range_maximum  = models.CharField(max_length=250, null=True)
  non_critical_range_minimum  = models.CharField(max_length=250, null=True)
  non_critical_range_maximum  = models.CharField(max_length=250, null=True)

  def __unicode__(self):
    return 'Lab Result %s' % self.id

