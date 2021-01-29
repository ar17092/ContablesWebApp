from .default import *

SECRET_KEY = '9ls_u0qO8TcrGhr68FP3h-3YkcV54l89_mL6A2brXcfXqfpJMDBgwfNOWydQKXjJZTg'

APP_ENV = APP_ENV_PRODUCTION

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://{username}:{passW}@sql3.freemysqlhosting.net:3306/{dbN}'.format(username='sql3389321',passW='WHeMCPE7ni',dbN='sql3389321')
