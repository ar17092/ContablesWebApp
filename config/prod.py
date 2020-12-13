from .default import *

SECRET_KEY = '9ls_u0qO8TcrGhr68FP3h-3YkcV54l89_mL6A2brXcfXqfpJMDBgwfNOWydQKXjJZTg'

APP_ENV = APP_ENV_PRODUCTION

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{username}:{passW}@localhost:3306/{dbN}'.format(username='root',passW='',dbN='contablesProd')
