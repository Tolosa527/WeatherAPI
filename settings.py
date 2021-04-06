import os

variables = os.environ

API_VERSION             = variables.get('API_VERSION')
API_ID                  = variables.get('API_ID')
OPENWEATHER_API_URL     = variables.get('OPENWEATHER_API_URL')
PROJECT_NAME            = variables.get('PROJECT_NAME')
REDIS_HOST              = variables.get('REDIS_HOST')
REDIS_PORT              = variables.get('REDIS_PORT')
REDIS_EXPIRATION_TIME   = variables.get('REDIS_EXPIRATION_TIME')
VERSION                 = variables.get('VERSION')  