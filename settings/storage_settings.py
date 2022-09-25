import json
import logging
import os

import environ
from django.conf import settings
from google.oauth2 import service_account

env = environ.Env(DEBUG=(bool, True))
env_file_name = env.get_value("ENV_FILE_NAME", default="envs/.local.env")
env_file = os.path.join(settings.BASE_DIR, env_file_name)
env_file = os.path.abspath(env_file)
logging.info(f"Loading env file: {env_file}")
if os.path.isfile(env_file):
    env.read_env(env_file)
    DEFAULT_FILE_STORAGE = "storages.backends.gcloud.GoogleCloudStorage"
    GS_BUCKET_NAME = env("GS_BUCKET_NAME")
    cred_path = "./envs/credentials.json"
    cred_path = os.path.join(settings.BASE_DIR, cred_path)
    if not os.path.exists(cred_path):
        with open(cred_path, "w") as f:
            data = json.loads(os.environ["GCP_CREDENTIALS"])
            json.dump(data, f)
    GS_CREDENTIALS = service_account.Credentials.from_service_account_file(cred_path)
    # add STORAGE to settings
    settings.DEFAULT_FILE_STORAGE = DEFAULT_FILE_STORAGE
    settings.GS_BUCKET_NAME = GS_BUCKET_NAME
    settings.GS_CREDENTIALS = GS_CREDENTIALS

else:
    logging.warning(f"Env file not found: {env_file}")
