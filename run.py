from app import create_app
import os
from decouple import config
settings_module= config('APP_SETTINGS_MODULE')
app = create_app(settings_module)