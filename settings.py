import os

variables = os.environ

API_VERSION               = variables.get('API_VERSION', None)
API_ID                    = variables.get('API_ID',None)
OPENWEATHER_API_URL       = variables.get('OPENWEATHER_API_URL', None)
PROJECT_NAME              = variables.get('PROJECT_NAME',None)
REDIS_HOST                = variables.get('REDIS_HOST', None)
REDIS_PORT                = variables.get('REDIS_PORT', None)
REDIS_EXPIRATION_TIME     = variables.get('REDIS_EXPIRATION_TIME', None)
VERSION                   = variables.get('VERSION', None)
API_TOKEN                 = variables.get('API_TOKEN', None)
METRICS_LOG               = variables.get('DEBUG_MODE', None)
DB_HOST                   = variables.get('DB_HOST', None)
DB_PORT                   = variables.get('DB_PORT', None)
DB_NAME                   = variables.get('DB_NAME', None)
USER_AUTHRIZED_COLLECTION = "users_authorized"