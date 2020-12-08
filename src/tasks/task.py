from celery_once import QueueOnce
from celery.utils.log import get_task_logger

from factory import make_celery

logger = get_task_logger(__name__)

celery_app = make_celery()


@celery_app.task(base=QueueOnce)
def test_task():
    logger.info('test_task called successfully')
