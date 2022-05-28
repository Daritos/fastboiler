from starlette.datastructures import CommaSeparatedStrings
import os
import pkgutil

from celery import Celery
from celery.utils.log import get_task_logger

ALLOWED_HOSTS = CommaSeparatedStrings(os.getenv("ALLOWED_HOSTS", ""))
API_V1_STR = "/api/v1"
PROJECT_NAME = "kubernetes-fastapi"

celery_tasks = [modname for importer, modname, ispkg in pkgutil.walk_packages(path=['./api/core/logic'], prefix='api.core.logic.', onerror=lambda x: None)]

# Initialize celery
celery = Celery(__name__)
celery.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://localhost:6379")
celery.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://localhost:6379")
celery.autodiscover_tasks(celery_tasks)
# Create logger - enable to display messages on task logger
celery_log = get_task_logger(__name__)