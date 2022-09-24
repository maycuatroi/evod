import logging
import os

import environ
from django.conf import settings

env = environ.Env(DEBUG=(bool, True))
env_file_name = env.get_value("ENV_FILE_NAME", default="envs/.local.env")
env_file = os.path.join(settings.BASE_DIR, env_file_name)
env_file = os.path.abspath(env_file)
logging.info(f"Loading env file: {env_file}")
if os.path.isfile(env_file):
    env.read_env(env_file)
    DATABASES = {"default": env.db()}
    if bool(os.getenv("USE_CLOUD_SQL_AUTH_PROXY", None)):
        print("Using Cloud SQL Proxy")
        DATABASES["default"]["HOST"] = "localhost"
        DATABASES["default"]["PORT"] = 5432
    # add DATABASES to settings
    settings.DATABASES = DATABASES

else:
    logging.warning(f"Env file not found: {env_file}")
