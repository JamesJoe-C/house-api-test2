import os

ACCOUNT_SID = os.environ['TWILIO_ACCOUNT_SID']
AUTH_TOKEN = os.environ['TWILIO_AUTH_TOKEN']
# generate token of phone confirmation
CONFIRMATION_SECRET_KEY = os.environ['CONFIRMATION_SECRET_KEY']
CONFIRMATION_SECURITY_PASSWORD_SALT = os.environ['CONFIRMATION_SECURITY_PASSWORD_SALT']
