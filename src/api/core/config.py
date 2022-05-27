from starlette.datastructures import CommaSeparatedStrings
import os

from celery import Celery
from celery.utils.log import get_task_logger

ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", ""))
API_V1_STR = "/api/v1"
PROJECT_NAME = "kubernetes-fastapi"

# Initialize celery
celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")
celery.conf.include = ['api.core.logic.*']
# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)