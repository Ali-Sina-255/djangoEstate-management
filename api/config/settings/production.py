from os import getenv, path

from dotenv import load_dotenv

from .base import *
from .base import BASE_DIR  # noqa

local_env_file = path.join(BASE_DIR, ".envs", ".env.local")
if path.isfile(local_env_file):
    load_dotenv(local_env_file)


SITE_NAME = getenv("SITE_NAME")


ALLOWED_HOSTS = []


ADMIN_URL = getenv("ADMIN_URL")
ADMIN_URL = getenv("ADMIN_URL")
ADMINS = [("Ali Sina", "alisinasultani52@gmaill.com")]
