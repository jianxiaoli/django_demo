from __future__ import absolute_import

from django_demo.celery import app

from django_demo import logger



@app.task
def test_celery():
    logger.info("celery test")