from os.path import abspath, dirname

#Definimos el directorio de la aplicación
BASE_DIR=dirname(dirname(abspath(__file__)))

SECRET_KEY = 'UlGBqgUCzdnXzYvugZxpQF689rFea0IdyPTNHBNfXaw2Zg66adpba_9xsZKRG4oNAQU'

SQLALCHEMY_TRACK_MODIFICATIONS = False

#Enviroments
APP_ENV_LOCAL = 'local'
APP_ENV_TESTING = 'testing'
APP_ENV_DEVELOPMENT = 'development'
APP_ENV_STAGING = 'staging'
APP_ENV_PRODUCTION = 'production'
APP_ENV = ''