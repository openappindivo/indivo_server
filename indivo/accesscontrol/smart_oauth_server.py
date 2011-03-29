"""
OAuth servers for SMArt apps

SMArt apps are per-user only.
"""

import oauth.oauth as oauth

from django.db import transaction

from indivo import models

import datetime, logging


class DataStore(oauth.OAuthStore):
  """
  Layer between Python OAuth and Django database
  for SMArt user applications 
  """

  def __get_app(self, consumer_key):
    try:
      return models.SmartApp.objects.get(consumer_key = consumer_key)
    except models.SmartApp.DoesNotExist:
      return None

  def __get_token(self, token_str, app=None):
    kwargs = {'token': token_str}
    if app: kwargs['installed_app__app'] = app

    try:
      return models.SmartAccessToken.objects.get(**kwargs)
    except models.SmartAccessToken.DoesNotExist:
      return None
    
  def verify_request_token_verifier(self, request_token, verifier):
    """
    Verify whether a request token's verifier matches
    The verifier is stored right in the request token itself
    """
    return request_token.verifier == verifier

  def lookup_consumer(self, consumer_key):
    """
    looks up a consumer
    """
    return self.__get_app(consumer_key)

  def create_request_token(self,  consumer, 
                           request_token_str, 
                           request_token_secret, 
                           verifier, 
                           oauth_callback, 
                           record_id=None):
    """
    take a RequestToken and store it.

    anything after request_token_secret is extra kwargs custom to this server.
    """
    
    # look for the record that this might be mapped to
    # IMPORTANT: if the user who authorizes this token is not authorized to admin the record, it will be a no-go
    record = None
    if record_id:
      try:
        record = models.Record.objects.get(id = record_id)
      except models.Record.DoesNotExist:
        pass

    # (BA) added record to the req token now that it can store it
    return models.SmartReqToken.objects.create(pha             = consumer, 
                                               token           = request_token_str, 
                                               token_secret    = request_token_secret, 
                                               verifier        = verifier, 
                                               oauth_callback  = oauth_callback, 
                                               record          = record)

  def lookup_request_token(self, consumer, request_token_str):
    """
    token is the token string
    returns a OAuthRequestToken

    consumer may be null.
    """
    try:
      # (BA) fix for consumer being null when we don't know yet who the consumer is
      if consumer:
        return models.SmartReqToken.objects.get(token = request_token_str, app = consumer)
      else:
        return models.SmartReqToken.objects.get(token = request_token_str)
    except models.SmartReqToken.DoesNotExist:
      return None

  def authorize_request_token(self, request_token, record, account=None):
    """
    Mark a request token as authorized by the given user,
    with the given additional parameters.

    This means the sharing has beeen authorized, so the Share should be added now.
    This way, if the access token process fails, a re-auth will go through automatically.

    The account is whatever data structure was received by the OAuthServer.
    """

    request_token.authorized_at = datetime.datetime.utcnow()
    request_token.authorized_by = account

    # store the share in the request token
    # added use of defaults to reduce code size if creating an object
    installed_app, create_p = models.SmartRecordInstalledApp.objects.get_or_create( record = record, 
                                                                                    app = request_token.app, 
                                                                                    defaults = {'authorized_at': request_token.authorized_at, 
                                                                                                'authorized_by': request_token.authorized_by})
      
    request_token.installed_app = installed_app
    request_token.save()
    

  def mark_request_token_used(self, consumer, request_token):
    """
    Mark that this request token has been used.
    Should fail if it is already used
    """
    new_rt = models.SmartReqToken.objects.get(app = consumer, token = request_token.token)

    # authorized?
    if not new_rt.authorized:
      raise oauth.OAuthError("Request Token not Authorized")

    new_rt.delete()

  def create_access_token(self, consumer, request_token, access_token_str, access_token_secret):
    """
    Store the newly created access token that is the exchanged version of this
    request token.
    
    IMPORTANT: does not need to check that the request token is still valid, 
    as the library will ensure that this method is never called twice on the same request token,
    as long as mark_request_token_used appropriately throws an error the second time it's called.
    """

    # create an access token for this share
    return models.SmartAccessToken.objects.create(
        token = access_token_str, 
        token_secret = access_token_secret, 
        account=request_token.authorized_by,
        installed_app = request_token.installed_app)

  
  def lookup_access_token(self, consumer, access_token_str):
    """
    token is the token string
    returns a OAuthAccessToken
    """
    return self.__get_token(token_str = access_token_str, app = consumer)

  def check_and_store_nonce(self, nonce_str):
    """
    store the given nonce in some form to check for later duplicates
    
    IMPORTANT: raises an exception if the nonce has already been stored
    """
    nonce, created = models.Nonce.objects.get_or_create(nonce = nonce_str)
    if not created:
      raise oauth.OAuthError("Nonce already exists")



OAUTH_SERVER = oauth.OAuthServer(store = DataStore())
