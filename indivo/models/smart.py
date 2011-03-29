"""
Models to support SMArt in Indivo

Using the existing Indivo data model seems like a bad idea (SMArt apps aren't Indivo apps),
so we recreate the data model needed here.

For now, SMArt apps will be whole-record only. No carenets.

Ben Adida
ben.adida@childrens.harvard.edu
"""

import urllib, datetime

from django.db import models
from django.conf import settings

from base import Object, Principal, INDIVO_APP_LABEL
from apps import *
from shares import *

class SmartApp(OAuthApp):
  """
  User applications
  """

  Meta = BaseMeta()

  # start_url (not really a template, but matches other model)
  start_url_template = models.CharField(max_length=500)

  # does the application have a user interface at all? (some are just background)
  has_ui = models.BooleanField(default=False)

  @property
  def permset(self):
    from indivo import accesscontrol
    return accesscontrol.get_permset('smartapp', self)

  def app_type(self):
    return "smart"

class SmartRecordInstalledApp(Object):
    class Meta:
        app_label = INDIVO_APP_LABEL
        unique_together = (('app', 'record'),)

    app = models.ForeignKey(SmartApp)
    record = models.ForeignKey('Record')

class SmartAccessToken(Principal, Token):
  # the token, secret, and PHA this corresponds to
  token = models.CharField(max_length=40)
  token_secret = models.CharField(max_length=60)

  # derived from a share
  installed_app = models.ForeignKey(SmartRecordInstalledApp)

  # who is this token on behalf of? Might be nulls here.
  account = models.ForeignKey('Account', null = True)

  # if null, it never expires, so BE CAREFUL
  expires_at = models.DateTimeField(null = True)

  # make sure email is set 
  def save(self, *args, **kwargs):
    self.email = "%s@accesstokens.smart-project.org" % self.token
    super(AccessToken,self).save(*args, **kwargs)
  
  @property
  def effective_principal(self):
    # is it a session for the account?
    if self.account:
      return self.account
    else:
      return self.installed_app.app

  @property
  def proxied_by(self):
    if self.account:
      return self.installed_app.app
    else:
      return None

  @property
  def permset(self):
    from indivo import accesscontrol
    return accesscontrol.get_permset('smartaccesstoken', self)

class SmartReqToken(Principal, Token):
  token = models.CharField(max_length=40)
  token_secret = models.CharField(max_length=60)
  verifier = models.CharField(max_length=60)
  oauth_callback = models.CharField(max_length=500, null=True)

  app = models.ForeignKey('SmartApp')

  # record or carenet
  record = models.ForeignKey('Record', null=True)

  # when authorized
  authorized_at = models.DateTimeField(null=True)

  # authorized by can be used to bind the request token first, before the authorized_at is set.
  authorized_by = models.ForeignKey('Account', null = True)

  # the share that this results in
  installed_app = models.ForeignKey('SmartRecordInstalledApp', null=True)

  # make sure email is set 
  def save(self, *args, **kwargs):
    self.email = "%s@requesttokens.smart-project.org" % self.token
    super(ReqToken,self).save(*args, **kwargs)
  
  @property
  def effective_principal(self):
    """
    a request token's identity is really the PHA it comes from.
    """
    return self.app

  @property
  def permset(self):
    from indivo import accesscontrol
    return accesscontrol.get_permset('smartrequesttoken', self)

  @property
  def authorized(self):
    # only look for authorized_at, because sometimes 
    # it's primed, and not authorized by a particular user
    return self.authorized_at != None
